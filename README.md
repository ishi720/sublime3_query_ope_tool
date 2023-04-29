# sublime3_query_ope_tool

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/c43257089f8e45d3b91d411b63e2b84f)](https://app.codacy.com/gh/ishi720/sublime3_query_ope_tool/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

### 概要

SublimeText3でurlの文字列操作を行えます。

### インストール方法(windows)

- SublimeText3のPackagesフォルダを開きます

> 例: %AppData%\Sublime Text 3\Packages

- git cloneします

```
git clone https://github.com/ishi720/sublime3_query_ope_tool.git
```

- 完了

### 使い方

- SublimeText3上で対象の文字列を選択
- Ctrl + Shift + p 
- コマンド実行


### コマンド

- url操作系

| コマンド | 実行内容 |
|:-|:-|
|ope url encode|URLのエンコード|
|ope url decode|URLのデコード|
|ope url line break|URLをgetパラメータごとに改行|
|ope url remove line break|URLに含まれる改行を削除|

- sql操作系

| コマンド | 実行内容 |
|:-|:-|
|ope sql line break|sqlを改行|
|ope sql remove line break|sqlに含まれる改行を削除|

- 表テーブルの変換

| コマンド | 実行内容 |
|:-|:-|
|ope table markdown to excel|markdownのテーブルを<br>Excelの表に貼り付けられる形式に変換|
|ope table excel to markdown|Excelの表を<br>markdownのテーブルに変換|


- javascriptのcodeをブックマークレット化

| コマンド | 実行内容 |
|:-|:-|
|ope bookmarklet edit|ブックマークレットに変換|
