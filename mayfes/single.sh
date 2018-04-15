file_end_name=".json"
file_start_name="./json_data/1stLayer/" # TODO:フォルダ名記入
for word in 明治大学 サポート 案内 大学 講座 m 行事 学校 月 中野 入学 マンション イベント 〜 # TODO:検索したい単語を記入
do
    filename=$file_start_name$word$file_end_name
    scrapy crawl single -o $filename -a word=$word
done
