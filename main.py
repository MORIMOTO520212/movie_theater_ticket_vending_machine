#   映画館　券売機システム YOHO CINEMA.
#   created 2020.12.18
#
#   動作環境：[Google Colaboratory], [Visual Studio Code], [Linux] 
#   ※[Jupyter Notebook] [Windows cmd] 非対応
#   
#   流れ
#   1.ようこそ！
#   2.性別確認
#   3.年齢確認
#   4.入力内容確認
#   5.年齢制限内の上映予定の映画一覧を表示
#       IPUTメンバー会員かつ鑑賞回数5回の場合　　一律1000円で表示
#       18歳～59歳までは　　　　一律1800円で表示
#       60歳～は　　一律1000円
#       日付　タイトル　上映時間　レイティング
#   6.タイムテーブル選択
#       空席状況 ◎余裕あり △残りわずか ✕満席
#   7.座席選択
#   8.内容確認
#
#   [リファレンス]
#   bashで16色表示するスクリプト用意しておくと便利 (https://gist.github.com/soramugi/7968403)
#   イオンシネマズの券売機でチケットを購入してみた (https://www.youtube.com/watch?v=iMuR0ATD48g)
#   TOHOシネマズ南大沢 スクリーン座席表（483人）- MDATA (https://zaseki.music-mdata.com/26198/1)
#   Google Colabの出力を定期的にクリアする方法 (https://www.366service.com/jp/qa/dfe7790f6cc709645fb160e50e504b22)

# empty - 余裕あり
# slight - 残りわずか
# full - 満席

import re, time, datetime, random

# ----- 初期設定 ----- #
# - IPUTメンバー会員 -
# True.[メンバー会員]  /  False.[メンバー会員でない]
iput_member = True
# この映画館での鑑賞回数
count = 5

movie_meta_contents = [
    {"title": "約束のネバーランド", "hour": "１１９分", "restricted": "Ｇ"},
    {"title": "ＳＴＡＮＤ　ＢＹ　ＭＥドラえもん２", "hour": "１１０分","restricted": "Ｇ"},
    {"title": "劇場版「鬼滅の刃」無限列車編", "hour": "１１０分", "restricted": "ＰＧ１２"},
    {"title": "映画　えんとつ町のプペル", "hour": "１１５分", "restricted": "Ｇ"},
    {"title": "劇場版　ポケットモンスター　ココ", "hour": "１１５分", "restricted": "Ｇ"},
    {"title": "吹替　ワンダーウーマン　１９８４", "hour": "１６５分", "restricted": "Ｇ"},
    {"title": "パウ・パトロール　カーレース大作戦ＧＯ！ＧＯ！", "hour": "５５分", "restricted": "Ｇ"},
    {"title": "君の名は。", "hour": "１１２分", "restricted": "Ｇ"},
    {"title": "魔女がいっぱい", "hour": "１０４分", "restricted": "Ｇ"},
    {"title": "天外者", "hour": "１０９分", "restricted": "Ｇ"},
    {"title": "ジョゼと虎と魚たち（＇２０）", "hour": "９８分", "restricted": "Ｇ"},
    {"title": "劇場版　Ｆａｔｅ／Ｇｒａｎｄ　Ｏｒｄｅｒ　神聖円卓領域キャメロット　全編　Ｗａｎｄｅｒｉｎｇ；Ａｇａｔｅｒｍ", "hour": "８９分", "restricted": "Ｇ"},
    {"title": "新解釈・三國志", "hour": "１１３分", "restricted": "Ｇ"},
    {"title": "天気の子", "hour": "１１１分", "restricted": "Ｇ"},
    {"title": "借りぐらしのアリエッティ", "hour": "９５分", "restricted": "Ｇ"},
    {"title": "ヱヴァンゲリヲン新劇場版：Ｑ", "hour": "１０６分", "restricted": "Ｇ"},
    {"title": "ぐらんぶる", "hour": "１０８分", "restricted": "ＰＧ１２"},
    {"title": "映画クレヨンしんちゃん　激突！ラクガキングダムとほぼ四人の勇者", "hour": "１０４分", "restricted": "Ｇ"},
    {"title": "映画ドラえもん　のび太の新恐竜", "hour": "１１１分", "restricted": "Ｇ"}
]

# 実行環境検証
console_clear_st = True
OS = 1 # google colab
try:
    from google.colab import output
except ImportError:
    console_clear_st = False
    OS = 2 # vscode linux
    import os

def console_clear():
    if console_clear_st:
        output.clear()
    else:
        os.system("cls")

def toem(n):
    # 半角数字から全角数字に変換する
    num = ["０","１","２","３","４","５","６","７","８","９"]
    em = ""
    for i in str(n):
        em += num[int(i)]
    return em

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
        if underline:code += "04"
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

vacant_list = [
    ["empty", "◎"], 
    ["slight", "△"], 
    ["full", "✕"]
]
screen_list = [
    "スクリーン０１", "スクリーン０２", "スクリーン０３", "スクリーン０４",
    "スクリーン０５", "スクリーン０６", "スクリーン０７", "スクリーン０８"
]
timetbl_list = [
    "０８：００～０９：５５", "１０：００～１１：５５", "１２：００～１３：５５",
    "１４：００～１５：５５", "１６：００～１７：５５", "１８：００～１９：５５",
    "２０：００～２１：５５"
]

now = datetime.datetime.now()
d_Y = now.strftime("%Y")
d_m = now.strftime("%m")
d_d = now.strftime("%d")

# タイムテーブル2~6
mdata = []
# 無作為抽出
while 0 < len(movie_meta_contents):
    if 1 != len(movie_meta_contents):
        m_i = random.randint(0, len(movie_meta_contents)-1)
    else: m_i = 0
    mdata.append(movie_meta_contents[m_i])
    movie_meta_contents.pop(m_i)

for m in mdata:
    m["date"] = "{}年{}月{}日".format(toem(d_Y),toem(d_m),toem(d_d)) # 日付
    timetbl = []
    timetbl_srt = list(range(7))
    lr = random.sample(timetbl_srt, len(timetbl_srt))
    for i in range(random.randint(2,5)):
        timetbl_srt[lr[i]] = False
    for i in timetbl_srt:
        if timetbl_srt[i]:
            timetbl.append([
                screen_list[random.randint(0,7)], 
                timetbl_list[i], 
                vacant_list[random.randint(0,2)][0]
            ])
    m["timetbl"] = timetbl # タイムテーブル

d = text_decoration.Decoration()
empty     = d.setting(mode="custom", fg="white",  bg="white")
white     = d.setting(mode="custom", fg="black",  bg="white")
strength  = d.setting(mode="custom", fg="yellow")
red       = d.setting(mode="custom", fg="red")
green     = d.setting(mode="custom", fg="green")
underline = d.setting(mode="custom", underline=True)

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
            if 0 == h: continue
            if h == height-1: break
            for w in range(width):
                if 0 == w: continue
                if w == width-1: break
                self.L[h][w] = "　"
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
        return no_vacant # 満席

    def MOVIE_LIST_CREATE(self ,page=1, view_num=4, row=4, col=1):
        width = self.width
        height = self.height
        table_num = view_num*page
        page = table_num - view_num
        for i in range(len(mdata)):
            if  i >= page and i < table_num:
                # 映画番号
                str_num = toem(i+1)
                title   = str_num+"．"+mdata[i]["title"]
                # 映画タイトル
                date       = mdata[i]["date"]
                hour       = mdata[i]["hour"]
                restricted = mdata[i]["restricted"]
                metadata   = re_uni_txt(f"　{date}　上映時間：{hour}　レイティング：{green + restricted + d.end()}")
                if "ＰＧ１２" == restricted:
                    metadata   = re_uni_txt(f"　{date}　上映時間：{hour}　レイティング：{red + restricted + d.end()}")
            
                for c in range(len(title)): # 1行目表示
                    self.L[row][c+col] = title[c]
                for c in range(len(metadata)): # 2行目表示
                    self.L[row+1][c+col] = metadata[c]
                for _ in range(width): # border
                    if not _: continue
                    if _ == width-1: continue 
                    self.L[row+2][_] = self.BD[self.os][4]
                row += 3
        return True
    
    def TIMETABLE_CREATE(self, f=False, page=1, view_num=4, row=4, col=1):
        width = self.width
        height = self.height
        no_vacant = [] # 満席の番号
        timetbl_lst = mdata[f]["timetbl"]
        table_num = view_num*page
        page = table_num - view_num
        for i in range(len(timetbl_lst)):
            if i >= page and i < table_num:
                # タイムテーブル番号
                str_num = toem(i+1)
                if "full" == timetbl_lst[i][2]:
                    no_vacant.append(str_num)
                screen = timetbl_lst[i][0] # スクリーン
                time = timetbl_lst[i][1] # 上映時間
                vacant = timetbl_lst[i][2] # 空席状況
                for i in range(len(vacant_list)):
                    if vacant == vacant_list[i][0]:
                        vacant = vacant_list[i][self.os] # 記号置き換え
                timetbl = str_num+"．"+screen+"　　"+time+"　"
                timetbl = [_ for _ in timetbl]
                timetbl.append(vacant)

                for c in range(len(timetbl)): # 1行目表示
                    self.L[row][c+col] = timetbl[c]
                for _ in range(width): # border
                    if not _: continue
                    if _ == width-1: continue 
                    self.L[row+1][_] = self.BD[self.os][4]
                row += 2
        return no_vacant

    def WINDOW(self): # 出力
        for line in self.L:
            for raw in line:
                print(raw, end="")
            print()


s = Screen()
s.SET_WINDOW(width=40, height=18, os=OS)


# 6.[タイムテーブル選択] - 製作中
#s.SET_TITLE("タイムテーブルを選択")
#if OS == 1:
#    s.SET_TEXT_CENTER("空席状況：◎余裕あり　△残りわずか　✕満席", row=1)
#if OS == 2:
#    text = ["空","席","状","況","：","◎ ","余","裕","あ","り","　","△ ","残","り","わ","ず","か","　","✕ ","満","席"]
#    s.SET_TEXT_CENTER(text, row=2)
#s.SET_TEXT_CENTER("選択するには数字を入力してください", row=4)
#s.SET_TEXT("戻る　ｂ　／　次へ　ｎ", position="bottom,left")
#s.TIMETABLE_CREATE(f=3, page=1, row=6) # f - mdataのインデックス
#s.WINDOW()

# 7.[座席選択 スクリーン画面]
#s.SET_TITLE("座席指定　スクリーン１")
#s.SET_TEXT("席の指定はアルファベットと数字を組み合わせて下さい。　例）Ａ０１", row=1)
#s.SET_TEXT(f"{white}白{d.end()}の席はすでに予約されています。", row=2)
#s.SET_TEXT("戻る　ｂ", position="bottom,left")
#s.SET_TEXT("指定する席のＩＤを入力してください。", position="bottom,right")
#no_vacant = s.SEAT_CREATE(row=4, vacant="empty") # 満席IDの配列を返す
#s.WINDOW()

# 8.[タイムテーブル選択]
#s.SET_TITLE("内容確認")
#s.SET_TEXT_CENTER("この内容でよろしいですか", row=4)
#s.SET_TEXT("タイトル", row=6, col=10)
#s.SET_TEXT("場所：スクリーン１", row=7, col=10)
#s.SET_TEXT("時間：０９：１０～１０：５０", row=8, col=10)
#s.SET_TEXT(["座","席","：","F ","15"], row=9, col=10)
#s.SET_TEXT("やり直す　ｎ　／　はい　ｙ", position="bottom,left")
#s.WINDOW()

usrdata = {"gender": "", "age":"", "mdata_idx": 0, "timetbl_idx": 0}
while True:
    s.CLEAR_WINDOW() # 画面初期化

    # 1.[ようこそ！]
    if 1 == S:
        console_clear()
        s.SET_TITLE(strength+"ＹＯＨＯ　ＫＩＮＥＭＡＳ"+d.end())
        s.SET_TEXT_CENTER("ようこそ！", row=5)
        s.SET_TEXT_CENTER("次へ進むにはエンターを押してください", row=8)
        s.WINDOW()
        input()
        S += 1
        continue

    # 2.[性別確認]
    if 2 == S:
        console_clear()
        s.SET_TITLE("確認１")
        s.SET_TEXT_CENTER("性別を選択してください。", row=5)
        s.SET_TEXT_CENTER("１．男性　／　２．女性", row=8)
        s.SET_TEXT("数字を入力してください", position="bottom,left")
        s.WINDOW()
        gen = input("数字>")
        if gen == "1":
            usrdata["gender"] = "male"
        if gen == "2":
            usrdata["gender"] = "female"
        S += 1
        continue

    # 3.[年齢確認]
    if 3 == S:
        console_clear()
        s.SET_TITLE("確認２")
        s.SET_TEXT_CENTER("年齢を入力してください。")
        s.SET_TEXT("数字を入力してください", position="bottom,left")
        s.WINDOW()
        age = input("数字>")
        usrdata["age"] = int(age)
        S += 1
        continue

    # 4.[入力内容確認]
    if 4 == S:
        console_clear()
        s.SET_TITLE("入力内容確認")
        s.SET_TEXT_CENTER("この内容で正しいですか。", row=5)
        s.SET_TEXT_CENTER("性別：男性", row=8)
        s.SET_TEXT_CENTER("年齢：１９歳", row=10)
        s.SET_TEXT("やり直す　ｎ　／　次へ進む　ｙ", position="bottom,left")
        s.WINDOW()
        res = input("入力>")
        if res == "y":
            S += 1
        elif res == "n":
            S = 2
        continue

    # 5.[年齢制限内の上映予定の映画一覧を表示]
    if 5 == S: 
        page = 1
        while True:
            console_clear()
            s.SET_TITLE("上映映画　一覧")
            s.SET_TEXT_CENTER("映画を選択するには番号を入力してください", row=2)
            s.MOVIE_LIST_CREATE(page=page) # ページを超えてエラーが出ないようにする
            s.SET_TEXT("戻る　ｂ　／　次へ　ｎ", position="bottom,left")
            s.WINDOW()
            res = input("入力>")
            if "n" == res: page += 1
            elif "b" == res: page -=1
            else:
                usrdata["mdata_idx"] = int(res)
                break
        S += 1
        continue

    # 6.[タイムテーブル選択]
    if 6 == S:
        while True:
            s.SET_TITLE("タイムテーブルを選択")
            if OS == 1:
                s.SET_TEXT_CENTER("空席状況：◎余裕あり　△残りわずか　✕満席", row=1)
            if OS == 2:
                text = ["空","席","状","況","：","◎ ","余","裕","あ","り","　","△ ","残","り","わ","ず","か","　","✕ ","満","席"]
                s.SET_TEXT_CENTER(text, row=2)
            s.SET_TEXT_CENTER("選択するには数字を入力してください", row=4)
            s.SET_TEXT("戻る　ｂ　／　次へ　ｎ", position="bottom,left")
            no_vacant = s.TIMETABLE_CREATE(f=usrdata["mdata_idx"], page=1, row=6) # f - mdataのインデックス
            s.WINDOW()
            res = input("数字>")
            if "n" == res: page += 1
            elif "b" == res: page -= 1
            else:
                if int(res) not in no_vacant:
                    usrdata["timetbl_idx"] = int(res)
                    break
                else:
                    s.CLEAR_WINDOW()
                    s.SET_TEXT_CENTER("選択した時間は満席です。")
                    s.WINDOW()
                    sleep(1)
        S += 1
        continue

    if 7 == S:
    if 8 == S:

    view_max = 3 # 一画面に表示するテーブル数

    movie_max = view_max
    movie_index = 0
    while True:
        tbl_len = len(mdata)
        print("選択するには映画の番号を入力してください")

        for i in range(len(tbl_len)):
            if i < movie_max and i >= movie_max - view_max:
                restricted = mdata[i]['restricted']
                if not restricted: restricted = "　"
                print("{}. {}　日付：{}　{}".format(str(i+1), mdata[i]['title'], mdata[i]['hour'], restricted))
        inp = input("\n前のページ b  /  次のページ n\n入力欄>")
        console_clear()

        t_max = tbl_len + (view_max - tbl_len % view_max)
        if not tbl_len % view_max:
            t_max = tbl_len

        if inp == "n":
            movie_max += view_max # next
            if movie_max > t_max:
                movie_max = view_max
            continue
        if inp == "b":
            movie_max -= view_max # back
            if movie_max == 0:
                movie_max = t_max
            continue

        try:
            movie_index = int(inp)-1 # 映画のインデックス
        except:
            print("不正な入力です。")
            continue
        break

    timetbl_max = view_max
    timetbl_index = 0
    while True:
        tbl_len = len(mdata[movie_index]["timetbl"])
        if OS == 1:
            print("空席状況：◎余裕あり　△残りわずか　✕満席")
        if OS == 2:
            print("空席状況：◎ 余裕あり　△ 残りわずか　✕ 満席") # 記号の後に空白必須
        print("選択するには数字を入力してください")

        for i in range(tbl_len):
            if i < timetbl_max and i >= timetbl_max - view_max:
                if OS == 1: # Google Colabratory
                    print("{}. {}　{}　{}".format(
                        str(i+1), mdata[movie_index]["timetbl"][i][0], mdata[movie_index]["timetbl"][i][1], mdata[movie_index]["timetbl"][i][2]))
                if OS == 2: # Windows Linux
                    print("{}. {}　{}　{} ".format(  # 記号の後に空白必須
                        str(i+1), mdata[movie_index]["timetbl"][i][0], mdata[movie_index]["timetbl"][i][1], mdata[movie_index]["timetbl"][i][2]))
        inp = input("\n前のページ b  /  次のページ n\n入力欄>")
        console_clear()

        t_max = tbl_len + (view_max - tbl_len % view_max)
        if not tbl_len % view_max:
            t_max = tbl_len

        if inp == "n":
            timetbl_max += view_max # next
            if timetbl_max > t_max:
                timetbl_max = view_max
            continue
        if inp == "b":
            timetbl_max -= view_max # back
            if timetbl_max == 0:
                timetbl_max = t_max
            continue
        try:
            timetbl_index = int(inp)-1 # 上映時間のインデックス
        except:
            print("不正な入力です。")
            console_clear()
            continue
        break

    while True:
        print("席を指定するにはアルファベットに続き数字を組み合わせた座席IDを入力してください")
        inp = input("座席ID>")
