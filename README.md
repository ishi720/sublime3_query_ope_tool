# sublime3_query_ope_tool

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8b238fa50f7d4928a52b665b808c6fe1)](https://www.codacy.com/app/ishi720/sublime3_query_ope_tool?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ishi720/sublime3_query_ope_tool&amp;utm_campaign=Badge_Grade)

### 概要

SublimeText3でurlの文字列操作を行えます。

### インストール方法(windows)

- SublimeText3のPackagesフォルダを開きます

> 例: C:\Users\%username%\AppData\Roaming\Sublime Text 3\Packages

- git cloneします

```
git clone https://github.com/ishi720/sublime3_query_ope_tool.git
```

- 完了

### 使い方

- SublimeText3上で対象の文字列を選択
- Ctrl + Shift + p 
- コマンド実行
  - ope url encode: URLのエンコード
  - ope url decode: URLのデコード
  - ope url line break: URLをgetパラメータごとに改行
  - ope url remove line break: 改行があるURLの改行を削除