# YTP
## 検索をする方法
```sh
cd YTP/mayfes/
vim query.sh # 検索したい単語を選択
bash query.sh
```

## query.shの仕様
### bashコマンドじゃないと動かない
```sh
# sh query.sh #XXX:これはだめ
bash query.sh
```
### 保存先は```YTP/mayfes/json_data/```
* このフォルダに存在するファイル名と一致する単語は検索しない
