#!/bin/bash
file_end_name=".json"
file_start_name="./json_data/2ndLayer/" # TODO:フォルダ名記入
for word in 公立 バー セキュリティ QR 数字 カメラ 操作 入力 使用 読み取り 画面 計画 支援 基本 葬儀 管理 行政 推進　# TODO:検索したい単語を記入
do
    filename=$file_start_name$word$file_end_name
    if [ ! -e $filename ]; then
        scrapy crawl single -o $filename -a word=$word
    fi
done
