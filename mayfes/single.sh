file_end_name=".json"
file_start_name="./json_data/" # TODO:フォルダ名記入
for word in 研究 教授 サークル ベンチャー 留学生 病院 部活 大学院 技術 学部 国際 科学 # TODO:検索したい単語を記入
do
    filename=$file_start_name$word$file_end_name
    scrapy crawl single -o $filename -a word=$word
done
