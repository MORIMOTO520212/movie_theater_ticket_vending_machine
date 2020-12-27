import re

def re_uni_txt(text):
    pattern = r".*?(\033\[.*?m).*" # fg
    result = re.match(pattern, text)
    uni_txt = []
    if result:
        fg = result.group(1)
        uni_txt.append(fg + text[len(fg)])
        for i in range(len(text)):
            if i == len(text)-6:
                uni_txt.append(text[i] +"\033[00m")
                break
            elif i > len(fg):
                uni_txt.append(text[i])
        return uni_txt
    return text

class Screen:
    BD = [0,
        ["┏","┓","┗","┛","━","┃","┃"],     # Google Colaboratory
        ["┏━","━┓","┗━","━┛","━━","┃ "," ┃"] # Windows, Linux
    ]
    def __init__(self):
        self.L = []

    def SET_WINDOW(self, width=50, height=5, os=1):  # width - スクリーン横幅
        self.width = width              # os   - 1 Google Colaboratory, 2 Windows Linux
        self.height = height
        self.os = os
        BD = self.BD
        # ウィンドウのリストを作成
        for _ in range(height):
            self.L.append(["  " for x in range(width)])
        
        for i in range(height):
            # 上部の角
            if i == 0:
                self.L[0][0]       = BD[os][0]
                self.L[0][width-1] = BD[os][1]
                continue
            # 下部の角
            if i == len(self.L)-1:
                self.L[len(self.L)-1][0]       = BD[os][2]
                self.L[len(self.L)-1][width-1] = BD[os][3]
                continue
            # 左右の縦線
            self.L[i][0]       = BD[os][5]
            self.L[i][width-1] = BD[os][6]
        # 上部と下部の線
        for i in range(width):
            if i != 0 and i != width-1:
                self.L[0][i]             = BD[os][4] # top border
                self.L[len(self.L)-1][i] = BD[os][4] # bottom border

    def SET_TITLE(self, title="ＮｏＴｉＴｌｅ"):
        width = self.width
        BD = self.BD
        os = self.os
        title = re_uni_txt(title) # カラーこ
        title_len = len(title)
        b_len = int((width - title_len) / 2)
        for i in range(width):
            x = i - b_len - 1

            if i == b_len:
                self.L[0][i] = BD[os][5]
            if i == b_len + title_len + 1:
                self.L[0][i] = BD[os][6]
            if i > b_len and x < title_len:
                self.L[0][i] = title[x]
    
    def SET_TEXT_CENTER(self, msg="Ｍｅｓｓａｇｅ．", row=False):
        width = self.width
        height = self.height
        if not row:
            c_height = int(height / 2) # 縦中央　自動設定
        else: 
            c_height = row # 個人設定
        b_len = int((width - len(msg)) / 2)
        for i in range(width):
            x = i - b_len - 1
            if i > b_len and x < len(msg):
                self.L[c_height][i] = msg[x]

    def SET_TEXT(self, msg="Ｍｅｓｓａｇｅ．", row=1):
        width = self.width
        height = self.height
        x = 0
        for h in range(height):
            if h < row: continue
            if h == height-1: break
            for i in range(width):
                if i == 0: continue
                if i == width-1: break
                if x >= len(msg): break
                self.L[h][i] = msg[x]
                x += 1

    def CLEAR_TEXT(self):
        pass

    def WINDOW(self): # 出力
        for line in self.L:
            for raw in line:
                print(raw, end="")
            print()



import os, time
OS = 2


s = Screen()
#   width=50 スクリーンの横幅
#   height=5 スクリーンの高さ
#   os=1 [Google Colaboratory],  os=2 [Windows] [Linux]
s.SET_WINDOW(width=50, height=15, os=OS)
# タイトルをセット (全角)
s.SET_TITLE("\033[37;01;40m一番上のタイトル\033[00m")
# 中央に文字を表示する
s.SET_TEXT_CENTER("中央に表示する文字")
# 左寄りに文字を表示する
# row=1 1行目から
s.SET_TEXT("左寄りに表示する文字", row=1)
s.WINDOW() # 出力
