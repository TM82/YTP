#!/bin/bash
file_end_name=".json"
file_start_name="./json_data/2ndLayer/" # TODO:フォルダ名記入
for word in 東大 目黒 周辺 フェリー 始発 終電 飛行機 電車 定期 製品 質問 ダウンロード お客様 修理 パスワード パソコン# TODO:検索したい単語を記入
do
    filename=$file_start_name$word$file_end_name
    if [ ! -e $filename ]; then
        scrapy crawl single -o $filename -a word=$word
    fi
done
