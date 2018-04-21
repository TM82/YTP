#!/bin/bash
file_end_name=".json"
file_start_name="./json_data/2ndLayer/" # TODO:フォルダ名記入
for word in 相談 曜日 受付 窓口 － 休 所在地 通報 紛争 解決 トップページ 本文 位置 者 方 公開 ご覧 検討 保険 ID 国立 推進 # TODO:検索したい単語を記入
do
    filename=$file_start_name$word$file_end_name
    if [ ! -e $filename ]; then
        scrapy crawl single -o $filename -a word=$word
    fi
done
