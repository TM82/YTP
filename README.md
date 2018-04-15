# YTP
## 導入
```sh
git clone git@github.com:TM82/YTP.git
```

## データ収集の流れ
1. 検索したい単語を決める
2. slackの \#pj_ytp_query で検索予定の単語を-checkする
3. -checkの返却値をquery.shに入力する
4. ```bash query.sh```
5. slackの \#pj_ytp_query で検索予定の単語を-setする
6. 収集したjsonファイルをコミットする
7. 収集したページから単語を抽出
8. 頻度、TF-IDF値等を算出する
9. 6を参考に1に戻る

## 検索をする方法
```sh
cd YTP/mayfes/
vim query.sh # TODO:検索したい単語を選択
bash query.sh
```

## query.shの仕様
### bashコマンドじゃないと動かない
```sh
# sh query.sh #XXX:これはだめ
bash query.sh
```
### 保存先は```YTP/mayfes/json_data/```
* このフォルダに存在するファイル名と一致する単語は検索しない。
    - 一度検索した単語を検索するのは無駄なため。
    - ただし、途中で処理を止めてしまった単語については、一度ファイルを削除してから実行する必要がある。
