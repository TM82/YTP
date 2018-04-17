file_end_name=".json"
file_start_name="./json_data/1stLayer/" # TODO:フォルダ名記入
for word in 校友 早稲田 図書館 オフィシャルサイト 活動 稲 国際 # TODO:検索したい単語を記入
do
    filename=$file_start_name$word$file_end_name
    scrapy crawl single -o $filename -a word=$word
done
