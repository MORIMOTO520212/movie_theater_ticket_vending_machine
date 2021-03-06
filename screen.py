# テスト用データ
vacant_list = [
    ["empty", "◎", "◎ "], 
    ["slight", "△", "△ "], 
    ["full", "✕", "✕ "]
]
mdata = [
    {
        'title': '映画クレヨンしんちゃん　激突！ラクガキングダムとほぼ四人の勇者', 'hour': '１０４分', 'restricted': 'Ｇ', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０５', '１０：００～１１：５５', 'empty'], 
            ['スクリーン０４', '１２：００～１３：５５', 'slight'], 
            ['スクリーン０６', '１４：００～１５：５５', 'empty'], 
            ['スクリーン０３', '２０：００～２１：５５', 'slight']
        ]
    },
    {
        'title': '約束のネバーランド', 'hour': '１１９分', 'restricted': 'Ｇ', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０６', '１２：００～１３：５５', 'slight'], 
            ['スクリーン０４', '１４：００～１５：５５', 'full'], 
            ['スクリーン０７', '２０：００～２１：５５', 'empty']
        ]
    }, 
    {
        'title': '劇場版　ポケットモンスター　ココ', 'hour': '１１５分', 'restricted': 'Ｇ', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０８', '１０：００～１１：５５', 'full'], 
            ['スクリーン０３', '１４：００～１５：５５', 'empty'], 
            ['スクリーン０６', '２０：００～２１：５５', 'full']
        ]
    }, 
    {
        'title': 'ジョゼと虎と魚たち（＇２０）', 'hour': '９８分', 'restricted': 'Ｇ', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０３', '１０：００～１１：５５', 'slight'], 
            ['スクリーン０１', '１２：００～１３：５５', 'slight'], 
            ['スクリーン０６', '１６：００～１７：５５', 'slight'], 
            ['スクリーン０３', '１８：００～１９：５５', 'slight'], 
            ['スクリーン０３', '２０：００～２１：５５', 'slight']
        ]
    }, 
    {
        'title': 'ヱヴァンゲリヲン新劇場版：Ｑ', 'hour': '１０６分', 'restricted': 'Ｇ', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０４', '１２：００～１３：５５', 'full'], 
            ['スクリーン０４', '１６：００～１７：５５', 'slight'], 
            ['スクリーン０５', '１８：００～１９：５５', 'empty']
        ]
    }, 
    {
        'title': 'ＳＴＡＮＤ　ＢＹ　ＭＥドラえもん２', 'hour': '１１０分', 'restricted': 'Ｇ', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０２', '１４：００～１５：５５', 'full'], 
            ['スクリーン０３', '１６：００～１７：５５', 'empty'], 
            ['スクリーン０５', '１８：００～１９：５５', 'slight']
        ]
    }, 
    {
        'title': 'パウ・パトロール　カーレース大作戦ＧＯ！ＧＯ！', 'hour': '５５分', 'restricted': 'Ｇ', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０４', '１０：００～１１：５５', 'empty'], 
            ['スクリーン０６', '１２：００～１３：５５', 'slight']
        ]
    }, 
    {
        'title': '映画ドラえもん　のび太の新恐竜', 'hour': '１１１分', 'restricted': 'Ｇ', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０７', '１６：００～１７：５５', 'slight'], 
            ['スクリーン０８', '２０：００～２１：５５', 'slight']
        ]
    }, 
    {
        'title': '吹替　ワンダーウーマン　１９８４', 'hour': '１６５分', 'restricted': 'Ｇ', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０６', '１８：００～１９：５５', 'slight'], 
            ['スクリーン０７', '２０：００～２１：５５', 'slight']
        ]
    }, 
    {
        'title': '映画　えんとつ町のプペル', 'hour': '１１５分', 'restricted': 'Ｇ', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０８', '１２：００～１３：５５', 'empty'], 
            ['スクリーン０６', '１４：００～１５：５５', 'full'], 
            ['スクリーン０１', '１６：００～１７：５５', 'empty'], 
            ['スクリーン０５', '１８：００～１９：５５', 'slight']
        ]
    }, 
    {
        'title': '借りぐらしのアリエッティ', 'hour': '９５分', 'restricted': 'Ｇ', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０７', '１４：００～１５：５５', 'full'], 
            ['スクリーン０６', '１６：００～１７：５５', 'full'], 
            ['スクリーン０３', '１８：００～１９：５５', 'empty'], 
            ['スクリーン０２', '２０：００～２１：５５', 'slight']
        ]
    }, 
    {
        'title': '魔女がいっぱい', 'hour': '１０４分', 'restricted': 'Ｇ', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０３', '１０：００～１１：５５', 'slight'], 
            ['スクリーン０１', '１２：００～１３：５５', 'full'], 
            ['スクリーン０４', '１８：００～１９：５５', 'slight'], 
            ['スクリーン０７', '２０：００～２１：５５', 'slight']
        ]
    }, 
    {
        'title': '君の名は。', 'hour': '１１２分', 'restricted': 'Ｇ', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０２', '１４：００～１５：５５', 'slight'], 
            ['スクリーン０８', '１６：００～１７：５５', 'empty']
        ]
    }, 
    {
        'title': 'ぐらんぶる', 'hour': '１０８分', 'restricted': 'ＰＧ１２', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０８', '１０：００～１１：５５', 'full'], 
            ['スクリーン０６', '１２：００～１３：５５', 'slight'], 
            ['スクリーン０７', '１６：００～１７：５５', 'slight']
        ]
    }, 
    {
        'title': '天気の子', 'hour': '１１１分', 'restricted': 'Ｇ', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０３', '２０：００～２１：５５', 'empty']
        ]
    }, 
    {
        'title': '新解釈・三國志', 'hour': '１１３分', 'restricted': 'Ｇ', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０１', '１４：００～１５：５５', 'slight'], 
            ['スクリーン０３', '１６：００～１７：５５', 'slight'], 
            ['スクリーン０３', '１８：００～１９：５５', 'empty']
        ]
    }, 
    {
        'title': '天外者', 'hour': '１０９分', 'restricted': 'Ｇ', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０３', '１２：００～１３：５５', 'slight'], 
            ['スクリーン０４', '１４：００～１５：５５', 'empty'], 
            ['スクリーン０７', '１６：００～１７：５５', 'slight'], 
            ['スクリーン０８', '２０：００～２１：５５', 'empty']
        ]
    }, 
    {
        'title': '劇場版　Ｆａｔｅ／Ｇｒａｎｄ　Ｏｒｄｅｒ　神聖円卓領域キャメロット　全編　Ｗａｎｄｅｒｉｎｇ；Ａｇａｔｅｒｍ', 'hour': '８９分', 'restricted': 'Ｇ', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０３', '１０：００～１１：５５', 'empty'], 
            ['スクリーン０７', '１４：００～１５：５５', 'empty'], 
            ['スクリーン０７', '１６：００～１７：５５', 'empty'], 
            ['スクリーン０２', '１８：００～１９：５５', 'full'], 
            ['スクリーン０７', '２０：００～２１：５５', 'empty']
        ]
    }, 
    {
        'title': '劇場版「鬼滅の刃」無限列車編', 'hour': '１１０分', 'restricted': 'ＰＧ１２', 'date': '２０２０年１２月３０日', 
        'timetbl': [
            ['スクリーン０３', '１０：００～１１：５５', 'empty'], 
            ['スクリーン０６', '１２：００～１３：５５', 'full'], 
            ['スクリーン０６', '１８：００～１９：５５', 'full']
        ]
    }
]
def toem(n):
    # 半角数字から全角数字に変換する
    num = ["０","１","２","３","４","５","６","７","８","９"]
    em = ""
    for i in str(n):
        em += num[int(i)]
    return em
# テスト用データ

import re, random, text_decoration

d = text_decoration.Decoration()
empty     = d.setting(mode="custom", fg="white",  bg="white")
white     = d.setting(mode="custom", fg="black",  bg="white")
strength  = d.setting(mode="custom", fg="yellow")
red       = d.setting(mode="custom", fg="red")
green     = d.setting(mode="custom", fg="green")
underline = d.setting(mode="custom", underline=True)

def re_uni_txt(text):
    # replace color script.
    # 一色のみ対応
    pattern = r".*?(\033\[.*?m).*"
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
        #   row      - 文字の縦の位置. 1 ~ max-width. 左寄せのみ.
        #   position - 文字の位置. [top] [center] [bottom] [right] [left] 2つ指定
        #              例）position="center,left"
        #   rowはpositionより優先
        width = self.width
        height = self.height
        try:
            msg = re_uni_txt(msg) # 装飾文字変換
        except: pass
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

    def CLEAR_WINDOW(self):
        width = self.width
        height = self.height
        os = self.os
        BD = self.BD
        for h in range(height):
            if h == height-1: break
            for w in range(width):
                if 0 == w: continue
                if w == width-1: break
                if 0 == h:
                    self.L[h][w] = BD[os][4] # top border
                else:
                    self.L[h][w] = "  "
        return False

    def SEAT_CREATE(self, row=3, vacant="empty"):
        width = self.width
        seat_label = ["A ", "B ", "C ", "D ", "E ", "  ", "F ", "G ", "H ", "I ", "J "]
        seat_num = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15"]
        no_vacant = []

        if "empty" == vacant: vacant = 5
        if "slight" == vacant: vacant = 1

        b_len = int((width - 30) / 2) # 横15席
        for h in range(len(seat_label)):
            if seat_label[h] != "  ":
                self.L[h+row][b_len] = seat_label[h]
                x = 0
                for i in range(width):
                    if i > b_len and i%2 == 1:
                        if not random.randint(0, vacant): # 5. 余裕あり 1. 残りわずか
                            self.L[h+row][i] = empty+"　"+d.end()
                            no_vacant.append(seat_label[h].replace(" ","")+seat_num[x]) # ex-> [A03, E01, F15]
                        else:
                            self.L[h+row][i] = seat_num[x]
                        x += 1
                    if i > b_len and i%2 == 0:
                        self.L[h+row][i] = "  "
                    if x == len(seat_num):
                        break
        return no_vacant, self.L


    def WINDOW(self, data=False): # 出力  [data(list)] 画面データをセットできる
        if data: L = data
        else: L = self.L
        for line in L:
            for raw in line:
                print(raw, end="")
            print()


import os, time, json
OS = 2
# width=50 スクリーンの横幅
# height=5 スクリーンの高さ
# os=1 [Google Colaboratory],  os=2 [Windows] [Linux]
s = Screen()
s.SET_WINDOW(width=40, height=18, os=OS)

# 7.[座席選択 スクリーン画面]
s.SET_TITLE("座席指定　スクリーン１")
s.SET_TEXT("席の指定はアルファベットと数字を組み合わせて下さい。　例）Ａ０１", row=1)
s.SET_TEXT(f"{white}白{d.end()}の席はすでに予約されています。", row=2)
s.SET_TEXT("戻る　ｂ", position="bottom,left")
s.SET_TEXT("指定する席のＩＤを入力してください。", position="bottom,right")
no_vacant, seatData = s.SEAT_CREATE(row=4, vacant="empty") # 満席IDの配列を返す
s.WINDOW()
seatData = json.dumps(seatData) # インスタンス変数の中身が常に変更されるのを防止する(原因不明)

s.CLEAR_WINDOW() # 画面初期化

print(json.loads(seatData))