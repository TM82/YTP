#!/bin/bash
file_end_name=".json"
file_start_name="./json_data/"
univ_name_array=("東京大学" "京都大学" "早稲田大学" "明治大学")
i=0
for univ in todai kyodai meiji waseda
do
    file_start_univ_name=$file_start_name$univ/
    for word in 研究 教授 サークル ベンチャー 留学生 病院 部活 大学院 技術 学部 国際 科学
    do
        filename=$file_start_univ_name$word$file_end_name
        scrapy crawl almighty -o $filename -a word=$word -a univ_name=${univ_name_array[i]}
    done
    i=$((i+1))
done
