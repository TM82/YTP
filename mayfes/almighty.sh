file_end_name=".json"
file_start_name="./json_data"
univ_name="京都大学" # TODO:大学名記入
univ_dir="/kyodai/" # TODO:フォルダ名記入
file_start_univ_name=$file_start_name$univ_dir
for word in タイムズ・ハイアー・エデュケーション 時計 特性 宇治 造形
do
    filename=$file_start_univ_name$word$file_end_name
    scrapy crawl almighty -o $filename -a univ_name=$univ_name -a word=$word
done
