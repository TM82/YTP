import sys
import MeCab
import functools
import itertools

# mc = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd -F%m,%f[0],%f[1],%f[2],')
mc = MeCab.Tagger('-F%m,%f[0],%f[1],%f[2],')

# 名詞を抽出する際の基本条件
basis_noun_conditions = {'except_nouns':['/', '(', ')', '>', '<', '-', '.', '...'],
                         'noun_types':['一般', '固有名詞','サ変接続'],
                         'noun_subtypes':[]}

# 動詞を抽出する際の基本条件
basis_verb_conditions = {'except_verbs':['さ','あり','でき','する','あり','できる','ある','考え','なり','なっ','思い','行っ',],
                         'verb_types':['自立']}

def make_noun_conditions(except_nouns = ['/', '(', ')', '>', '<', '-', '.'],
                         noun_types = ['一般', '固有名詞','サ変接続'],
                         noun_subtypes = []):
    return {'except_nouns':except_nouns, 'noun_types':noun_types, 'noun_subtypes':noun_subtypes}

def make_verb_conditions(except_verbs = ['さ','あり','でき','する','あり','できる','ある','考え','なり','なっ','思い','行っ',],
                         verb_types = ['自立']):
    return {'except_verbs':except_verbs, 'verb_types':verb_types}


def extract_words(noun_conditions, verb_conditions, text):
    """
    文字列を形態素解析し、名詞と動詞を抽出する
    variables
    ----------
    text: str
    名詞、動詞を抽出したい文字列
    noun_conditions: dict(list(str), list(str), list(str))
    抽出する名詞の条件
    verb_conditions: dict(list(str), list(str))
    抽出する動詞の条件
    return
    ----------
    extracted_words_list: list(str)
    抽出した名詞、動詞のリスト
    """
    def impose_conditions(noun_conditions, verb_conditions, word_and_speech_tuple):
        if ((word_and_speech_tuple[0] not in verb_conditions['except_verbs'] and \
            word_and_speech_tuple[1] == '動詞' and \
            word_and_speech_tuple[2] in verb_conditions['verb_types']) or \
            (word_and_speech_tuple[0] not in noun_conditions['except_nouns'] and \
            word_and_speech_tuple[1] == '名詞' and \
            word_and_speech_tuple[2] in noun_conditions['noun_types'] and \
            (noun_conditions['noun_subtypes'] == [] or word_and_speech_tuple[3] in noun_conditions['noun_subtypes']))):

            return word_and_speech_tuple[0]

    word_and_speech = mc.parse(text).split(',')[:-1]
    word_and_speech_tuple_list = list(zip(*[iter(word_and_speech)]*4))
    extracted_words_list = list(filter(None, map(functools.partial(impose_conditions, noun_conditions, verb_conditions), word_and_speech_tuple_list)))

    return extracted_words_list



def extract_noun(noun_conditions, text):
    """
    文字列を形態素解析し、名詞だけを抽出する
    variables
    ----------
    text: str
    名詞を抽出したい文字列
    noun_conditions: dict(list(str), list(str), list(str))
    抽出する名詞の条件
    return
    ----------
    extracted_noun_list: list(str)
    抽出した名詞のリスト
    """

    def impose_conditions(word_and_speech_tuple, noun_conditions):
        if (word_and_speech_tuple[0] not in noun_conditions['except_nouns'] and \
            word_and_speech_tuple[1] == '名詞' and \
            word_and_speech_tuple[2] in noun_conditions['noun_types']):

            if (noun_conditions['noun_subtypes'] == [] or word_and_speech_tuple[3] in noun_conditions['noun_subtypes']):
                return word_and_speech_tuple[0]

    word_and_speech = mc.parse(text).split(',')[:-1]
    word_and_speech_tuple_list = list(zip(*[iter(word_and_speech)]*4))
    extracted_noun_list = list(filter(None, map(functools.partial(impose_conditions, noun_conditions=noun_conditions), word_and_speech_tuple_list)))

    return extracted_noun_list

def extract_cooccurrence_noun(noun_conditions, text):
    extracted_noun_list = extract_noun(noun_conditions, text)

    return list(itertools.combinations(extracted_noun_list, 2))

import collections as col
import pandas as pd

def ranking_by_frequency(words_list, n_extract=None, reverse=False):
    """
    頻度による対象の文書の単語ランキングを出力する。
    variables
    ----------
    words_list: list(str)
    対象の文書の単語のlist
    n_extract: ranking_tuple_list
    第何位までランキングを出力するか？
    """
    count_tuple_list = col.Counter(words_list)
    if n_extract is None:
        ranking_tuple_list = count_tuple_list.most_common()
    else:
        ranking_tuple_list = count_tuple_list.most_common(n_extract)

    # if reverse:
    #     return count_tuple_list.most_common()[-n_extract:-1]

    return ranking_tuple_list

from gensim import corpora
from gensim import models
from operator import itemgetter

def ranking_by_tfidf(full_texts, target_words_list, n_extract=None):
    """
    tfidfによる対象の文書の単語ランキングを出力する。
    variables
    ----------
    full_texts: list(list(str))
    全文書の単語のlistが含まれているlist
    target_words_list: list(str)
    対象の文書の単語のlist
    n_extract: int
    第何位までランキングを出力するか？
    """
    dictionary = corpora.Dictionary(full_texts)
    id2token = {v: k for k, v in dictionary.token2id.items()}
    full_corpus = map(dictionary.doc2bow, full_texts)
    target_corpus = map(dictionary.doc2bow, [target_words_list])
    tfidf_model = models.TfidfModel(full_corpus)

    if n_extract is None:
        ranking_by_id = sorted(list(tfidf_model[target_corpus])[0], key=itemgetter(1), reverse=True)
    else:
        ranking_by_id = sorted(list(tfidf_model[target_corpus])[0], key=itemgetter(1), reverse=True)[0:n_extract]

    map_ranking = map(functools.partial(lambda id2token, tp: ((id2token[tp[0]], tp[1])), id2token), ranking_by_id)

    return list(map_ranking)

def ranking2df(ranking, column_names):
    return pd.DataFrame(list(zip(*ranking)) ,index=column_names).T
