#   映画館　券売機システム YOHO CINEMA.
#   created 2020.12.18
#
#   ##1##
#   いままでの券売機システムには、ヒューマンエラーの処理やUXがなく使いにくかったのが問題だと思ったので改良した。
#
#   ##2##
#   画面の中に文字が密になっていてわかりにくいので、さらに文字を簡略化し配置を整え、かつ理解しやすいように文を整理する。
#   
#   ##3##
#   bashで16色表示するスクリプト用意しておくと便利 (https://gist.github.com/soramugi/7968403)
#   イオンシネマズの券売機でチケットを購入してみた (https://www.youtube.com/watch?v=iMuR0ATD48g)
#   TOHOシネマズ南大沢 スクリーン座席表（483人）- MDATA (https://zaseki.music-mdata.com/26198/1)
#   Google Colabの出力を定期的にクリアする方法 (https://www.366service.com/jp/qa/dfe7790f6cc709645fb160e50e504b22)
#
#
#
#   動作環境：[Google Colaboratory], [Visual Studio Code], [Linux] 
#   ※[Jupyter Notebook] [Windows cmd] 非対応
#
#
#   [初期設定]
#   これらの情報は画面から入力できないようにする
#   True  IPUTメンバー会員  /  False  IPUTメンバー会員でない
iput_member = True
#   この映画館での鑑賞回数
count = 6


import re, datetime, random, json
from time import sleep



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
    {"title": "劇場版　Ｆａｔｅ／Ｇｒａｎｄ　Ｏｒｄｅｒ　神聖円卓領域キャメロット　全編", "hour": "８９分", "restricted": "Ｇ"},
    {"title": "新解釈・三國志", "hour": "１１３分", "restricted": "Ｇ"},
    {"title": "天気の子", "hour": "１１１分", "restricted": "Ｇ"},
    {"title": "借りぐらしのアリエッティ", "hour": "９５分", "restricted": "Ｇ"},
    {"title": "ヱヴァンゲリヲン新劇場版：Ｑ", "hour": "１０６分", "restricted": "Ｇ"},
    {"title": "ぐらんぶる", "hour": "１０８分", "restricted": "ＰＧ１２"},
    {"title": "映画クレヨンしんちゃん　激突！ラクガキングダムとほぼ四人の勇者", "hour": "１０４分", "restricted": "Ｇ"},
    {"title": "映画ドラえもん　のび太の新恐竜", "hour": "１１１分", "restricted": "Ｇ"},
    {"title": "銀魂　ＴＨＥ　ＦＩＮＡＬ", "hour": "１０４分", "restricted": "ＰＧ１２"},
    {"title": "新感染半島　ファイナル・ステージ", "hour": "１１６分", "restricted": "Ｇ"},
    {"title": "サイレント・トーキョー", "hour": "９９分", "restricted": "Ｇ"},
    {"title": "ＬＩＰＸＬＩＰ　ＦＩＬＭＸＬＩＶＥ", "hour": "９０分", "restricted": "Ｇ"},
    {"title": "トイ・ストーリー４", "hour": "１００分", "restricted": "Ｇ"},
    {"title": "ベイマックス", "hour": "１０８分", "restricted": "Ｇ"},
    {"title": "アナと雪の女王", "hour": "１０９分", "restricted": "Ｇ"},
    {"title": "シュガー・ラッシュ", "hour": "１０８分", "restricted": "Ｇ"},
    {"title": "ズートピア", "hour": "１１１分", "restricted": "Ｇ"},
    {"title": "ルイスと未来の泥棒", "hour": "１０２分", "restricted": "Ｇ"},
    {"title": "チキンリトル", "hour": "８１分", "restricted": "Ｇ"},
    {"title": "ロボッツ", "hour": "９１分", "restricted": "Ｇ"},
    {"title": "ウォーリー", "hour": "１０３分", "restricted": "Ｇ"}
]

# 実行環境検出
console_clear_st = True
OS = 1 # google colab
try: from google.colab import output
except ImportError:
    console_clear_st = False
    OS = 2 # vscode linux
    import os

def console_clear():
    if console_clear_st:
        output.clear()
    else:
        os.system("cls")

def toem(n): # 半角数字から全角数字に変換する
    num = ["０","１","２","３","４","５","６","７","８","９"]
    em = ""
    for i in str(n):
        em += num[int(i)]
    return em

def re_uni_txt(text):
    # replace color script.
    # 一色のみ対応
    pattern = r".*?(\033\[.*?m).*"
    res = re.match(pattern, text)
    uni_txt = []
    if res:
        dec = res.group(1)
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

gender_toJa = { # gender to Japanese
    "male": "男性",
    "female": "女性"
}
vacant_list = [
    ["empty", "◎", "◎ "], 
    ["slight", "△", "△ "], 
    ["full", "✕", "✕ "]
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
restricted_toAge = {
    "Ｇ": 0,       #  0<=age
    "ＰＧ１２": 12, # 12<=age 保護者の同意で鑑賞可能
    "Ｒ１５＋": 15, # 15<=age
    "Ｒ１８＋": 18  # 18<=age
}
# 性別,　年齢,　座席ID,　料金,　mdata index,　mdata timetbl index
def usrdata_init(): return {"gender": "", "age":"","seat_id": "","billing":"", "mdata_idx": 0, "timetbl_idx": 0}

now = datetime.datetime.now()
d_Y = now.strftime("%Y")
d_m = now.strftime("%m")
d_d = now.strftime("%d")

# 上映映画 仮想タイムテーブル作成
mdata = []
while 0 < len(movie_meta_contents):
    if 1 != len(movie_meta_contents):
        m_i = random.randint(0, len(movie_meta_contents)-1)
    else: m_i = 0
    mdata.append(movie_meta_contents[m_i])
    movie_meta_contents.pop(m_i)

for m in mdata:
    m["date"] = "{}年{}月{}日".format(toem(d_Y),toem(d_m),toem(d_d))
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
    m["timetbl"] = timetbl

d = Decoration()
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

        return no_vacant, self.L # 満席 座席表データ


    def MOVIE_LIST_CREATE(self ,page=1, view_num=4, row=4, col=1):
        width = self.width
        page_end = int(len(mdata)/view_num)
        if len(mdata)%view_num: page_end += 1
        if page > page_end:
            page = page_end
        if page < 1:
            page = 1
        table_num_end = view_num*page
        table_num_start = table_num_end - view_num
        if len(mdata)%view_num:
            page_end += 1
        for i in range(len(mdata)):
            if  i >= table_num_start and i < table_num_end:
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
                    if c == width-2: break  # 折り返しなし
                    self.L[row][c+col] = title[c]
                for c in range(len(metadata)): # 2行目表示
                    self.L[row+1][c+col] = metadata[c]
                for _ in range(width): # border
                    if not _: continue
                    if _ == width-1: continue 
                    self.L[row+2][_] = self.BD[self.os][4]
                row += 3
        return page
    
    def TIMETABLE_CREATE(self, f=False, page=1, view_num=4, row=4, col=1):
        width = self.width
        no_vacant = [] # 満席の番号
        timetbl_lst = mdata[f]["timetbl"]
        table_num = view_num*page
        page = table_num - view_num
        for i in range(len(timetbl_lst)):
            if i >= page and i < table_num:
                # タイムテーブル番号
                str_num = toem(i+1)
                if "full" == timetbl_lst[i][2]:
                    no_vacant.append(i+1)
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

    def WINDOW(self, data=False): # 出力  [data(list)] 画面データをセットできる
        if data: L = data
        else: L = self.L
        for line in L:
            for raw in line:
                print(raw, end="")
            print()

s = Screen()
s.SET_WINDOW(width=40, height=18, os=OS)

usrdata = []
ud_idx = 0
page = 1
S = 1
seat_created = False
while True:
    s.CLEAR_WINDOW() # 画面初期化
    console_clear()

    # 1.[ようこそ！]
    if 1 == S:
        s.SET_TITLE(strength+"ＹＯＨＯ　ＫＩＮＥＭＡＳ"+d.end())
        s.SET_TEXT_CENTER("ようこそ！", row=5)
        s.SET_TEXT_CENTER("次へ進むにはエンターを押してください", row=8)
        s.WINDOW()
        input()
        usrdata.append(usrdata_init())
        ud_idx = len(usrdata)-1
        S += 1
        continue

    # 2.[性別確認]
    if 2 == S:
        s.SET_TITLE("確認１")
        s.SET_TEXT_CENTER("性別を選択してください。", row=5)
        s.SET_TEXT_CENTER("１．男性　／　２．女性", row=8)
        s.SET_TEXT("数字を入力してください", position="bottom,left")
        s.WINDOW()
        S += 1
        gen = input("数字 >")
        if gen == "1":
            usrdata[ud_idx]["gender"] = "male"
        elif gen == "2":
            usrdata[ud_idx]["gender"] = "female"
        else:
            S = 29
        continue

    if S == 29: # 2 エラー処理
        s.SET_TEXT_CENTER("不正な入力です", row=5)
        s.SET_TEXT_CENTER("半角英数字で入力してください。", row=7)
        s.WINDOW()
        sleep(1)
        S = 2
        continue

    # 3.[年齢確認]
    if 3 == S:
        s.SET_TITLE("確認２")
        s.SET_TEXT_CENTER("年齢を入力してください。")
        s.SET_TEXT("数字を入力してください", position="bottom,left")
        s.WINDOW()
        age = input("数字 >")
        try:
            age = int(age) # エラー処理
        except:
            S == 39
            continue
        usrdata[ud_idx]["age"] = age
        # 支払い
        if iput_member and 5 == count: # スタンプカード
            usrdata[ud_idx]["billing"] = "１０００"
        elif 18 <= age and 59 >= age: # 一般
            usrdata[ud_idx]["billing"] = "１８００"
        elif 60 < age: # シニア
            usrdata[ud_idx]["billing"] = "１１００"
        else: # 小中高校生
            usrdata[ud_idx]["billing"] = "１０００"
        S += 1
        continue

    if S == 39: # 3 エラー処理
        s.SET_TEXT_CENTER("不正な入力です", row=5)
        s.SET_TEXT_CENTER("半角英数字で入力してください。", row=7)
        s.WINDOW()
        sleep(1)
        S = 3
        continue

    # 4.[入力内容確認]
    if 4 == S:
        s.SET_TITLE("入力内容確認")
        s.SET_TEXT_CENTER("この内容で正しいですか。", row=5)
        s.SET_TEXT_CENTER(f"性別：{gender_toJa[usrdata[ud_idx]['gender']]}", row=8)
        s.SET_TEXT_CENTER(f"年齢：{toem(usrdata[ud_idx]['age'])}歳", row=10)
        s.SET_TEXT("やり直す　ｎ　／　次へ進む　ｙ", position="bottom,left")
        s.WINDOW()
        res = input("入力 >").upper()
        if res == "Y":
            S += 1
        elif res == "N":
            S = 2
        else:
            S = 49
        continue

    if S == 49: # 4 エラー処理
        s.SET_TEXT_CENTER("不正な入力です", row=5)
        s.SET_TEXT_CENTER("半角英数字で入力してください。", row=7)
        s.WINDOW()
        sleep(1)
        S = 4
        continue

    # 5.[年齢制限内の上映予定の映画一覧を表示]
    if 5 == S:
        s.SET_TITLE("上映映画　一覧")
        s.SET_TEXT_CENTER("映画を選択するには番号を入力してください", row=2)
        page = s.MOVIE_LIST_CREATE(page=page) # ページを超えてエラーが出ないようにする
        s.SET_TEXT("前へ　ｂ　／　次へ　ｎ", position="bottom,left")
        s.WINDOW()
        res = input("入力>").upper()
        if "N" == res: page += 1
        elif "B" == res: page -= 1
        else:
            try:
                m_restricted = mdata[int(res)-1]["restricted"]
                if restricted_toAge[m_restricted] <= usrdata[ud_idx]["age"]:
                    usrdata[ud_idx]["mdata_idx"] = int(res)-1
                    S += 1
                elif "ＰＧ１２" == m_restricted:
                    usrdata[ud_idx]["mdata_idx"] = int(res)-1
                    S = 57
                else:
                    S = 58
            except: S = 59
        continue

    if 57 == S: # 5 PG12 規制
        # １２歳未満は親の同意が必要です　同意しないｎ／同意するｙ
        s.SET_TEXT_CENTER("１２歳未満は親の同意が必要です。")
        s.SET_TEXT("同意しない　ｎ　／　同意する　ｙ", position="bottom,left")
        s.WINDOW()
        res = input("入力>").upper()
        if "Y" == res: S = 6
        elif "N" == res: S = 5
        else: S = 59 # エラー処理
        continue

    if 58 == S: # 5 R15+ R18+ 規制
        s.SET_TEXT_CENTER(
            toem(restricted_toAge[m_restricted])+"歳未満はこの映画は鑑賞することができません。"
        )
        s.WINDOW()
        sleep(1)
        S = 5
        continue

    if 59 == S: # 5 エラー処理
        s.SET_TEXT_CENTER("不正な入力です", row=5)
        s.SET_TEXT_CENTER("半角英数字で入力してください。", row=7)
        s.WINDOW()
        sleep(1)
        S = 5
        continue

    page = 1

    # 6.[タイムテーブルを選択]
    if 6 == S:
        s.SET_TITLE("タイムテーブルを選択")
        if OS == 1:
            s.SET_TEXT_CENTER("空席状況：◎余裕あり　△残りわずか　✕満席", row=1)
        if OS == 2:
            text = ["空","席","状","況","：","◎ ","余","裕","あ","り","　","△ ","残","り","わ","ず","か","　","✕ ","満","席"]
            s.SET_TEXT_CENTER(text, row=2)
        s.SET_TEXT_CENTER("選択するには数字を入力してください", row=4)
        s.SET_TEXT("戻る　ｚ　　前へ　ｂ　／　次へ　ｎ", position="bottom,left")
        no_vacant = s.TIMETABLE_CREATE(f=usrdata[ud_idx]["mdata_idx"], page=page, row=6) # f - mdataのインデックス
        s.WINDOW()
        res = input("入力 >").upper()
        if "N" == res: page += 1
        elif "B" == res: page -= 1
        elif "Z" == res: S -= 1
        else:
            if int(res) not in no_vacant:
                usrdata[ud_idx]["timetbl_idx"] = int(res)-1 # index
                S += 1
            else: S = 69
        continue
    
    if 69 == S: # 6 エラー処理
        s.CLEAR_WINDOW()
        s.SET_TEXT_CENTER("選択した時間は満席です。")
        s.WINDOW()
        sleep(1)
        S = 6
        continue

    # 7.[座席選択 スクリーン画面] 席入力でエラーが出た後座席表が出ない
    if 7 == S:
        mdata_idx   = usrdata[ud_idx]["mdata_idx"]
        timetbl_idx = usrdata[ud_idx]["timetbl_idx"]
        screen  = mdata[mdata_idx]["timetbl"][timetbl_idx][0]
        s.SET_TITLE(f"座席指定　{screen}")
        s.SET_TEXT("席の指定はアルファベットと数字を組み合わせて下さい。　例）Ａ０１", row=1)
        s.SET_TEXT(f"{white}白色{d.end()}の席はすでに予約されています。", row=2)
        s.SET_TEXT_CENTER("１階席", row=3)
        s.SET_TEXT_CENTER("２階席", row=9)
        s.SET_TEXT("戻る　ｂ", position="bottom,left")
        s.SET_TEXT("指定する席のＩＤを入力してください。", position="bottom,right")
        mdata_idx = usrdata[ud_idx]["mdata_idx"]
        timetbl_idx = usrdata[ud_idx]["timetbl_idx"]
        vacant = mdata[mdata_idx]["timetbl"][timetbl_idx][2]

        if not seat_created:
            no_vacant, seatData = s.SEAT_CREATE(row=4, vacant=vacant) # 満席IDの配列を返す
            seatData = json.dumps(seatData) # インスタンス変数の中身が常に変更されるのを防止する(原因不明)
            s.WINDOW()
        else:
            s.WINDOW(json.loads(seatData))
        seat_created = True
        res = input("座席ID >").upper()
        if "B" == res:
            S -= 1
        elif res not in no_vacant:
            pattern = r"([A-Z]{1})([0-9]{2})"
            res = re.match(pattern, res)
            if not res:
                S = 79
                continue
            usrdata[ud_idx]["seat_id"] = res.group()
            S += 1
        else:
            S = 78
        continue

    if 78 == S: # 7 満席処理
        s.SET_TEXT_CENTER("指定した席は満席です")
        s.WINDOW()
        sleep(1)
        S = 7
        continue

    if 79 == S: # 7 エラー処理
        s.SET_TEXT_CENTER("不正な入力です", row=5)
        s.SET_TEXT_CENTER("半角英数字で、アルファベットに続き、数字と組み合わせてください。", row=7)
        s.SET_TEXT_CENTER("例）Ａ１０", row=8)
        s.WINDOW()
        sleep(1)
        S = 7
        continue

    # 8.[内容確認]
    if 8 == S:
        # IPUTメンバー会員かつ鑑賞回数5回の場合　　一律1000円で表示
        # 18歳～59歳までは　　　　一律1800円で表示
        # 60歳～は　　一律1000円
        mdata_idx   = usrdata[ud_idx]["mdata_idx"]
        timetbl_idx = usrdata[ud_idx]["timetbl_idx"]
        title       = mdata[mdata_idx]["title"]
        date        = mdata[mdata_idx]["date"]
        seat_id     = usrdata[ud_idx]["seat_id"]
        screen      = mdata[mdata_idx]["timetbl"][timetbl_idx][0]
        time        = mdata[mdata_idx]["timetbl"][timetbl_idx][1]
        billing     = usrdata[ud_idx]["billing"]
        s.SET_TITLE("内容確認")
        s.SET_TEXT_CENTER("この内容でよろしいですか", row=4)
        s.SET_TEXT_CENTER(title, row=6)
        s.SET_TEXT(f"日付：{date}", row=7, col=10)
        s.SET_TEXT(f"場所：{screen}", row=8, col=10)
        s.SET_TEXT(f"時間：{time}", row=9, col=10)
        s.SET_TEXT(["座","席","：",f"{seat_id[:1]} ", seat_id[1:]], row=10, col=10)
        s.SET_TEXT(f"料金：{billing}円", row=11, col=10)
        s.SET_TEXT("やり直す　ｎ　／　はい　ｙ", position="bottom,left")
        s.WINDOW()
        res = input("入力 >").upper()
        if "N" == res:
            S = 5
        elif "Y" == res:
            S += 1
        else:
            S = 89
        continue

    if S == 89: # 8 エラー処理
        s.SET_TEXT_CENTER("不正な入力です", row=5)
        s.SET_TEXT_CENTER("半角英数字で入力してください。", row=7)
        s.WINDOW()
        sleep(1)
        S = 8
        continue

    # 9.[もう一枚チケットを購入するかどうか]
    if 9 == S:
        s.SET_TITLE("内容確認")
        s.SET_TEXT_CENTER("もう一枚チケットを購入しますか。")
        s.SET_TEXT("終了　ｎ　／　はい　ｙ", position="bottom,left")
        s.WINDOW()
        res = input("入力 >").upper()
        if "N" == res:
            break
        elif "Y" == res:
            S = 1
            seat_created = False # 座席表データを新たに作成する
        else:
            S = 99
    
    if S == 99: # 9 エラー処理
        s.SET_TEXT_CENTER("不正な入力です", row=5)
        s.SET_TEXT_CENTER("半角英数字で入力してください。", row=7)
        s.WINDOW()
        sleep(1)
        S = 9
        continue

console_clear()

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
for usr in usrdata:
    print(f"[購入者情報]\n  性別：{gender_toJa[usr['gender']]}\n  年齢：{usr['age']}\n\n[チケット情報]\n  タイトル：{mdata[usr['mdata_idx']]['title']}\n\
  鑑賞日付：{mdata[usr['mdata_idx']]['date']}\n  上映時間：{mdata[usr['mdata_idx']]['timetbl'][usr['timetbl_idx']][1]}\n  上映スクリーン：{mdata[usr['mdata_idx']]['timetbl'][usr['timetbl_idx']][0]}\n\
  座席：{usr['seat_id']}\n\n[チケット一枚の単価]\n  {usr['billing']}円\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

bill_sum = 0
for usr in usrdata: bill_sum += int(usr["billing"]) # 合計金額

print(f"\n[チケットの購入枚数]\n{toem(len(usrdata))}枚\n[支払い料金の合計金額]\n{toem(bill_sum)}円")