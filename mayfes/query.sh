#!/bin/bash
file_end_name=".json"
file_start_name="./json_data/2ndLayer/" # TODO:フォルダ名記入
for word in 書 確認 au カタログ 料金 保険 方法 ページ 電話 支払い 証明 明細 手続き 金額 問い合わせ　# TODO:検索したい単語を記入
do
    filename=$file_start_name$word$file_end_name
    if [ ! -e $filename ]; then
        scrapy crawl single -o $filename -a word=$word
    fi
done
