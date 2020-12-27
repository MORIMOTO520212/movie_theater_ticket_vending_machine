import re, random, text_decoration

d = text_decoration.Decoration()
empty = d.setting(mode="custom", fg="white", bg="white")
white = d.setting(mode="custom", fg="black", bg="white")

def re_uni_txt(text):
    pattern = r".*?(\033\[.*?m).*" # color script
    result = re.match(pattern, text)
    uni_txt = []
    if result:
        dec = result.group(1)
        text = text.replace(dec, "@").replace("\033[00m", "#")
        i = 0
        while i < len(text):
            uni_txt.append(text[i])
            if text[i] == "@":
                if i:
                    uni_txt[i-1] += dec
                    uni_txt.remove("@")
                else:
                    uni_txt[i] = dec + text[i+1]
                    i += 1
            elif text[i] == "#":
                uni_txt[i-2] += "\033[00m"
            i += 1
        try:
            uni_txt.remove("#")
        except: pass
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
        self.width = width                           # os - 1 [Google Colaboratory], 2 [Windows] [Linux]
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
        title = re_uni_txt(title) # 装飾文字変換
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
        msg = re_uni_txt(msg) # 装飾文字変換
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

    def SEAT_CREATE(self, row=3, vacant="◎"):
        width = self.width
        seat_label = ["A ", "B ", "C ", "D ", "E ", "  ", "F ", "G ", "H ", "I ", "J "]
        seat_num = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15"]
        no_vacant = []

        if "◎" == vacant: vacant = 5
        if "△" == vacant: vacant = 1

        b_len = int((width - 30) / 2) # 横15席
        for h in range(len(seat_label)):
            if seat_label[h] != "  ":
                self.L[h+row][b_len] = seat_label[h]
                x = 0
                for i in range(width):
                    if i > b_len and i%2 == 1:
                        if not random.randint(0, vacant): # 5. 余裕あり 1. 残りわずか
                            self.L[h+row][i] = empty+"　"+d.end()
                            no_vacant.append(seat_label[h]+seat_num[x]) # ex-> [A03, E01, F15]
                        else:
                            self.L[h+row][i] = seat_num[x]
                        x += 1
                    if i > b_len and i%2 == 0:
                        self.L[h+row][i] = "  "
                    if x == len(seat_num):
                        break
        return no_vacant

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
#s.SET_WINDOW(width=50, height=15, os=OS)
# タイトルをセット (全角)
#s.SET_TITLE("一番上のタイトル")
# 中央に文字を表示する
#s.SET_TEXT_CENTER("中央に表示する文字")
# 左寄りに文字を表示する
# row=1 1行目から
#s.SET_TEXT("左寄りに表示する文字", row=1)
#s.WINDOW() # 出力

# 8 座席選択
s.SET_WINDOW(width=40, height=18, os=OS)
s.SET_TITLE("スクリーン１")
s.SET_TEXT("席を指定するにはアルファベットと数字を組み合わせて下さい。　例）Ａ０１", row=1)
s.SET_TEXT(f"{white}白{d.end()}の席はすでに予約されています。", row=2)
no_vacant = s.SEAT_CREATE(row=4, vacant="◎") # 満席IDの配列を返す
s.WINDOW()