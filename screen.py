import re, random, text_decoration

d = text_decoration.Decoration()
empty     = d.setting(mode="custom", fg="white", bg="white")
white     = d.setting(mode="custom", fg="black", bg="white")
strength  = d.setting(mode="custom", fg="yellow", bg="black")
underline = d.setting(mode="custom", underline=True)

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
            c_height = int(height / 2)-1 # 縦中央　自動設定
        else: 
            c_height = row # 個人設定
        b_len = int((width - len(msg)) / 2)
        for i in range(width):
            x = i - b_len - 1
            if i > b_len and x < len(msg):
                self.L[c_height][i] = msg[x]

    def SET_TEXT(self, msg="Ｍｅｓｓａｇｅ．", row=False, col=False, position="top,left"):
        #   arguments
        #   msg      - 全角の文字を指定する.
        #   row      - 文字の縦の位置. 1が一番上. 左寄せのみ.
        #   position - 文字の位置. [top] [center] [bottom] [right] [left] 2つ指定
        #              例）position="center,left"
        #   rowはpositionより優先
        width = self.width
        height = self.height
        msg = re_uni_txt(msg) # 装飾文字変換
        position = position.split(",")
        if not row:
            if "top"    == position[0]: row = 1
            if "center" == position[0]: row = int(height / 2)
            if "bottom" == position[0]: row = height-2
        if not col:
            if "left"   == position[1]: col = 1
            if "right"  == position[1]: col = width - len(msg)-1
        
        x = 0
        for h in range(height):
            if h < row: continue
            if h == height-1: break
            for c in range(width):
                if c < col: continue
                if c == width-1: break # 終端
                if x >= len(msg): break
                self.L[h][c] = msg[x]
                x += 1
        return True


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
        return no_vacant # 満席

    def WINDOW(self): # 出力
        for line in self.L:
            for raw in line:
                print(raw, end="")
            print()



import os, time
OS = 2

s = Screen()
# width=50 スクリーンの横幅
# height=5 スクリーンの高さ
# os=1 [Google Colaboratory],  os=2 [Windows] [Linux]
s.SET_WINDOW(width=40, height=18, os=OS)
# タイトルをセット (全角)
#s.SET_TITLE("ＹＯＨＯ　ＫＩＮＥＭＡＳ")
# 中央に文字を表示する
#s.SET_TEXT("ようこそ！")
# 左寄りに文字を表示する
# row=1 1行目から
#s.SET_TEXT("文字", position="top,right")
#s.WINDOW() # 出力

# 1.[ようこそ！]
#s.SET_TITLE(f"{strength}ＹＯＨＯ　ＫＩＮＥＭＡＳ{d.end()}")
#s.SET_TEXT_CENTER("ようこそ！", row=5)
#s.SET_TEXT_CENTER("次へ進むにはエンターを押してください", row=8)
#s.WINDOW()

# 2.[性別確認]
#s.SET_TITLE("確認１")
#s.SET_TEXT_CENTER("性別を選択してください。", row=5)
#s.SET_TEXT_CENTER("１．男性　／　２．女性", row=8)
#s.SET_TEXT("数字を入力してください", position="bottom,left")
#s.WINDOW()

# 3.[年齢確認]
#s.SET_TITLE("確認２")
#s.SET_TEXT_CENTER("年齢を入力してください。")
#s.SET_TEXT("数字を入力してください", position="bottom,left")
#s.WINDOW()

# 4.[入力内容確認]
#s.SET_TITLE("入力内容確認")
#s.SET_TEXT_CENTER("この内容で正しいですか。", row=5)
#s.SET_TEXT_CENTER("性別：男性", row=8)
#s.SET_TEXT_CENTER("年齢：１９歳", row=10)
#s.SET_TEXT("やり直す　ｎ　／　次へ進む　ｙ", position="bottom,left")
#s.WINDOW()

# 5.[年齢制限内の上映予定の映画一覧を表示]

# 6.[]


# 7.[座席選択 スクリーン画面]
#s.SET_WINDOW(width=40, height=18, os=OS)
#s.SET_TITLE("スクリーン１")
#s.SET_TEXT("席の指定はアルファベットと数字を組み合わせて下さい。　例）Ａ０１", row=1)
#s.SET_TEXT(f"{white}白{d.end()}の席はすでに予約されています。", row=2)
#s.SET_TEXT("戻る　ｂ", row=16)
#no_vacant = s.SEAT_CREATE(row=4, vacant="◎") # 満席IDの配列を返す
#s.WINDOW()