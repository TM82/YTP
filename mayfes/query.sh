#!/bin/bash
file_end_name=".json"
file_start_name="./json_data/2ndLayer/" # TODO:フォルダ名記入
for word in 交流 関西 成田空港 ターミナル フライト 駐車 航空 中国 注意 KB 改定 報酬 帝京大学 予算 # TODO:検索したい単語を記入
do
    filename=$file_start_name$word$file_end_name
    if [ ! -e $filename ]; then
        scrapy crawl single -o $filename -a word=$word
    fi
done
