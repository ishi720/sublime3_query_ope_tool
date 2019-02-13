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
