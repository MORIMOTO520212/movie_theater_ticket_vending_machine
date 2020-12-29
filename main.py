#   映画館　券売機システム YOHO CINEMA.
#   created 2020.12.18
#
#   動作環境：[Google Colaboratory], [Windows], [Linux]  ※[Jupyter Notebook] 非対応
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

import os

# empty - 余裕あり
# slight - 残りわずか
# full - 満席


# ----- 初期設定 ----- #
# - IPUTメンバー会員 -
# True.[メンバー会員]  /  False.[メンバー会員でない]
iput_member = True
# この映画館での鑑賞回数
count = 5


# 実行環境検証
console_clear_st = True
OS = 1
try:
    from google.colab import output
except ImportError:
    console_clear_st = False
    OS = 2
    import os

def console_clear():
    if console_clear_st:
        output.clear()
    else:
        os.system("cls")



console_clear()
input("- YOHO KINEMAS -\nようこそ！\nエンターを押してください")
console_clear()

while True:
    gen = input("性別を選択してください\n1.男性 2.女性\n数字を入力してください\n数字>")
    console_clear()
    age = input("年齢を入力してください\n数字>")
    console_clear()
    if gen == "1":
        gen_p = "男性"
    if gen == "2":
        gen_p = "女性"
    res = input(f"この内容で正しいですか\n性別：{gen_p}\n年齢：{age}\nやり直す n  /  はい y>")
    console_clear()
    if res == "y": break


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