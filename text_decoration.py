# 文字色　背景色
#   setting(mode=モード, fg=文字色, bg=背景色, bold=強調, underline=下線)
#   [モード]
#   light   ライト
#   select  選択
#   hilight ハイライト
#   [文字色 / 背景色]
#   black, red, green, yellow, blue, magenta, cyan, white
#   [強調]
#   True 強調する
#   [下線]
#   True 下線を引く
class Decoration:
    def setting(self, mode, fg="white", bg=False, bold=False, underline=False):
        code = "\033["
        if fg:
            if fg == "black": code += "30"
            if fg == "red": code += "31"
            if fg == "green": code += "32"
            if fg == "yellow": code += "33"
            if fg == "blue": code += "34"
            if fg == "magenta": code += "35"
            if fg == "cyan": code += "36"
            if fg == "white": code += "37"
            if bg or bold or underline: code += ";"
        if bg:
            if bg == "black": code += "40"
            if bg == "red": code += "41"
            if bg == "green": code += "42"
            if bg == "yellow": code += "43"
            if bg == "blue": code += "44"
            if bg == "magenta": code += "45"
            if bg == "cyan": code += "46"
            if bg == "white": code += "47"
            if bold or underline: code += ";"
        if bold:
                code += "01"
                if underline: code += ";"
        if underline:
            code += "04"

        code += "m"

        if mode == "light":
            self.light_fgbg = code
        if mode == "select":
            self.select_fgbg = code
        if mode == "hilight":
            self.hilight_fgbg = code
        if mode == "custom":
            return code
    def light(self):
        return self.light_fgbg # 文字色;背景色
    def select(self):
        return self.select_fgbg
    def hilight(self):
        return self.hilight_fgbg
    def end(self):
        return "\033[00m"

d = Decoration()
# ライト
d.setting(mode="light", fg="black", bg="white")
# 選択
d.setting(mode="select", fg="white", bg="red")
# ハイライト
d.setting("hilight", "red", "white", True, True)
# オリジナル
custom = d.setting(mode="custom", fg="red", bg="white", bold=True, underline=True)
# 出力
#print(d.hilight()+"チケット"+d.end())
#print(custom+"チケット"+d.end())