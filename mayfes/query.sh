#!/bin/bash
file_end_name=".json"
file_start_name="./json_data/" # TODO:フォルダ名記入
for word in 請求 病院 # TODO:検索したい単語を記入
do
    filename=$file_start_name$word$file_end_name
    if [ ! -e $filename ]; then
        scrapy crawl single -o $filename -a word=$word
    fi
done
