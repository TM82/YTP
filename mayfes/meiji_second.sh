file_end_name=".json"
file_start_name="./json_data/meiji/"
for word in プロデューサー ワイドショー 支部 駿河台 校友 紫紺 リバティアカデミー 本校 杉原 早稲田大学 ドラマ 即日
do
    filename=$file_start_name$word$file_end_name
    scrapy crawl meiji_second -o $filename -a word=$word
done
