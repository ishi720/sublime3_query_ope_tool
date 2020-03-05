import sublime
import sublime_plugin

import urllib.parse
import re


def checkSel(sel_range):
    """選択範囲の確認
    """
    if sel_range.empty():
        sublime.message_dialog("選択範囲が指定されていません")
        exit()


class escapeXml(sublime_plugin.TextCommand):
    """XML特殊文字をエスケープ
    """
    def run(self, edit):
        # 選択範囲の取得
        sel_area = self.view.sel()

        # 選択範囲の確認
        checkSel(sel_area[0])

        for i in range(len(sel_area)):
            # 選択範囲の文字列取得
            sel_string = self.view.substr(sel_area[i])

            text = sel_string
            
            text = re.sub( '&', '&amp;', text) # &は最初に変換する
            text = re.sub( '<', '&lt;', text)
            text = re.sub( '>', '&gt;', text)
            text = re.sub( '"', '&quot;', text)
            text = re.sub( '\'', '&apos;', text)

            # 選択範囲と入替え
            self.view.replace(edit, sel_area[i], text)


class unescapeXml(sublime_plugin.TextCommand):
    """XML特殊文字を戻す
    """
    def run(self, edit):
        # 選択範囲の取得
        sel_area = self.view.sel()

        # 選択範囲の確認
        checkSel(sel_area[0])

        for i in range(len(sel_area)):
            # 選択範囲の文字列取得
            sel_string = self.view.substr(sel_area[i])

            text = sel_string
            
            text = re.sub( '&lt;', '<', text)
            text = re.sub( '&gt;', '>', text)
            text = re.sub( '&quot;','"', text)
            text = re.sub( '&apos;', '\'', text)
            text = re.sub( '&amp;', '&', text) # &amp;は最後に変換する

            # 選択範囲と入替え
            self.view.replace(edit, sel_area[i], text)



class encodeUrl(sublime_plugin.TextCommand):
    """urlのエンコードする
    """
    def run(self, edit):
        # 選択範囲の取得
        sel_area = self.view.sel()

        # 選択範囲の確認
        checkSel(sel_area[0])

        for i in range(len(sel_area)):
            # 選択範囲の文字列取得
            sel_string = self.view.substr(sel_area[i])

            # urlエンコード
            url = urllib.parse.quote(sel_string)

            # 選択範囲と入替え
            self.view.replace(edit, sel_area[i], url)


class decodeUrl(sublime_plugin.TextCommand):
    """urlをデコードする
    """
    def run(self, edit):
        # 選択範囲の取得
        sel_area = self.view.sel()

        # 選択範囲の確認
        checkSel(sel_area[0])

        for i in range(len(sel_area)):
            # 選択範囲の文字列取得
            sel_string = self.view.substr(sel_area[i])

            # urlデコード
            url = urllib.parse.unquote(sel_string)

            # 選択範囲と入替え
            self.view.replace(edit, sel_area[i], url)


class getParaLineBreak(sublime_plugin.TextCommand):
    """URLをgetパラメータで改行する
    """
    def run(self, edit):
        # 選択範囲の取得
        sel_area = self.view.sel()

        # 選択範囲の確認
        checkSel(sel_area[0])

        for i in range(len(sel_area)):
            # 選択範囲の文字列取得
            sel_string = self.view.substr(sel_area[i])

            # 改行を入れる
            url = re.sub('(\&|\?|#)', "\n\\1", sel_string)

            # 選択範囲と入替え
            self.view.replace(edit, sel_area[i], url)


class removeLineBreak(sublime_plugin.TextCommand):
    """改行を削除する
    """
    def run(self, edit):
        # 選択範囲の取得
        sel_area = self.view.sel()

        # 選択範囲の確認
        checkSel(sel_area[0])

        for i in range(len(sel_area)):
            # 選択範囲を文字列として取得
            sel_string = self.view.substr(sel_area[i])

            # 改行を削る
            url = re.sub('\n', '', sel_string)

            # 選択範囲と入替え
            self.view.replace(edit, sel_area[i], url)


class bookmarkletEdit(sublime_plugin.TextCommand):
    """ブックマークレットを作成する
    """
    def run(self, edit):
        # 選択範囲の取得
        sel_area = self.view.sel()

        # 選択範囲の確認
        checkSel(sel_area[0])

        for i in range(len(sel_area)):
            # 選択範囲を文字列として取得
            sel_string = self.view.substr(sel_area[i])

            #コメントアウトを削る
            code = re.sub('/\*.*?\*/', '', sel_string, flags=(re.MULTILINE | re.DOTALL))
            code = re.sub('//.*', '', code)

            # 改行を削る
            code = re.sub('\n', '', code)

            # urlをエンコードする
            code = urllib.parse.quote(code)

            # ブックマークレットの形式にする
            code = 'javascript:(function(){' + code + '})();'

            # 選択範囲と入替え
            self.view.replace(edit, sel_area[i], code)



class sqlLineBreak(sublime_plugin.TextCommand):
    """SQLを改行する
    """
    def run(self, edit):
        # 選択範囲の取得
        sel_area = self.view.sel()

        # 選択範囲の確認
        checkSel(sel_area[0])

        for i in range(len(sel_area)):
            # 選択範囲の文字列取得
            sel_string = self.view.substr(sel_area[i])

            keyword_list = [
                'SELECT','UPDATE','SET','INSERT INTO','VALUES','DELETE','ADD','CHANGE',
                'FROM','WHERE','AND','OR','ORDER BY','GROUP BY','HAVING','LIMIT','OFFSET',
                'CREATE TABLE','ENGINE'
            ]
            regexp = '(' + " |".join(keyword_list) + ')'

            # 改行を入れる
            url = re.sub(regexp, "\n\\1", sel_string, flags=re.IGNORECASE)

            # 戦闘の改行を削る
            url = re.sub('^\n', '', url)

            # 選択範囲と入替え
            self.view.replace(edit, sel_area[i], url)


class sqlRemoveLineBreak(sublime_plugin.TextCommand):
    """改行を削除する
    """
    def run(self, edit):
        # 選択範囲の取得
        sel_area = self.view.sel()

        # 選択範囲の確認
        checkSel(sel_area[0])

        for i in range(len(sel_area)):
            # 選択範囲を文字列として取得
            sel_string = self.view.substr(sel_area[i])

            # 整形する
            url = re.sub('\n', " ", sel_string) # 改行を削る
            url = re.sub('\s+', " ", url) # スぺースを整える

            # 選択範囲と入替え
            self.view.replace(edit, sel_area[i], url)


class convertTableMdToExcel(sublime_plugin.TextCommand):
    """markdownテーブルをExcelテーブルに変換
    """
    def run(self, edit):
        # 選択範囲の取得
        sel_area = self.view.sel()

        # 選択範囲の確認
        checkSel(sel_area[0])

        for i in range(len(sel_area)):

            # 選択範囲を文字列として取得
            sel_string = self.view.substr(sel_area[i])

            # 整形する
            url = re.sub('\|.*?[-:]+?.*?\|.*?\n', "", sel_string, flags=re.MULTILINE) # |--|--|の行を削る
            url = re.sub(' *\| *', "\t", url, flags=re.IGNORECASE) # パイプをタブに変換する
            url = re.sub('^\t', "", url, flags=re.MULTILINE) # 先頭のタブを削る
            url = re.sub('\t$', "", url, flags=re.MULTILINE) # 末尾のタブを削る
            url = re.sub('(\S*)<br>(\S)', "\"\\1\n\\2\"", url, flags=re.MULTILINE) # セル内の改行コードの変換



            # 選択範囲と入替え
            self.view.replace(edit, sel_area[i], url)
