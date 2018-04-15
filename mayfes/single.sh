file_end_name=".json"
file_start_name="./json_data/1stLayer/" # TODO:フォルダ名記入
for word in 学部 月 医学部 紹介 マンション 内科 案内 病院 三田 教授 請求 日吉キャンパス # TODO:検索したい単語を記入
do
    filename=$file_start_name$word$file_end_name
    scrapy crawl single -o $filename -a word=$word
done
