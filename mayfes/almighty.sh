file_end_name=".json"
file_start_name="./json_data"
univ_name="東京大学" # TODO:大学名記入
univ_dir="/todai/" # TODO:フォルダ名記入
file_start_univ_name=$file_start_name$univ_dir
for word in 研究 教授 サークル ベンチャー 留学生 病院 部活 大学院 技術 学部 国際 科学
do
    filename=$file_start_univ_name$word$file_end_name
    scrapy crawl almighty -o $filename -a univ_name=$univ_name -a word=$word
done
