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
    def setting(self, mode, fg, bg, bold=False, underline=False):
        if fg == "black": fg = "\033[30;"
        if fg == "red": fg = "\033[31;"
        if fg == "green": fg = "\033[32;"
        if fg == "yellow": fg = "\033[33;"
        if fg == "blue": fg = "\033[34;"
        if fg == "magenta": fg = "\033[35;"
        if fg == "cyan": fg = "\033[36;"
        if fg == "white": fg = "\033[37;"
        if bold: fg += "01;"
        if underline: fg += "04;"
        if bg == "black": bg = "40m"
        if bg == "red": bg = "41m"
        if bg == "green": bg = "42m"
        if bg == "yellow": bg = "43m"
        if bg == "blue": bg = "44m"
        if bg == "magenta": bg = "45m"
        if bg == "cyan": bg = "46m"
        if bg == "white": bg = "47m"
        if mode == "light":
            self.light_fgbg = fg+bg
        if mode == "select":
            self.select_fgbg = fg+bg
        if mode == "hilight":
            self.hilight_fgbg = fg+bg
        if mode == "custom":
            return fg+bg
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
print(d.hilight()+"チケット"+d.end())
print(custom+"チケット"+d.end())