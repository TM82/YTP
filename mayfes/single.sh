file_end_name=".json"
file_start_name="./json_data/1stLayer/" # TODO:フォルダ名記入
for word in 研究 学生 キャンパス 情報 サイト 大学 大学院 入試 総合 消費 生活協同組合 発信 本郷 駒場 平成 教育 医療 社会 # TODO:検索したい単語を記入
do
    filename=$file_start_name$word$file_end_name
    scrapy crawl single -o $filename -a word=$word
done
