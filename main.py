#   映画館　券売機システム
#   created 2020.12.18
#
#   動作環境：Windows, Linux, Google Colaboratory
#
#   流れ
#   初期設定：動作環境がGoogle Colaboratoryの場合は１、Windows, Linuxの場合は２を打って下さい。
#   1.性別確認
#   2.年齢確認
#   3.年齢制限内の上映予定の映画一覧を表示
#       IPUTメンバー会員かつ鑑賞回数5回の場合　　一律1000円で表示
#       18歳～59歳までは　　　　一律1800円で表示
#       60歳～は　　一律1000円
#   4.映画選択
#       タイトル　日付　上映時間　閲覧年齢制限　レイティング　空席状況 ◎余裕あり △残りわずか ✕完売
#   5.タイムテーブル選択
#   6.チケット選択 何枚買うか
#   7.座席選択
#   8.内容確認
#   9.支払い方法
#   10.チケット発券
#
#   [リファレンス]
#   bashで16色表示するスクリプト用意しておくと便利 (https://gist.github.com/soramugi/7968403)
#   イオンシネマズの券売機でチケットを購入してみた (https://www.youtube.com/watch?v=iMuR0ATD48g)
#   Google Colabの出力を定期的にクリアする方法 (https://www.366service.com/jp/qa/dfe7790f6cc709645fb160e50e504b22)

import os

mdata = [
    {
        "title": "約束のネバーランド",
        "date": "２０２０年１２月２４日",
        "hour": "１３５分",
        "restricted": False,
        "vacant": "△",
        "timetbl": [
            ["スクリーン０１", "０９：４５～１２：００"],
            ["スクリーン０３", "１０：５５～１３：１０"],
            ["スクリーン０１", "１２：２５～１４：４０"],
            ["スクリーン０１", "１５：１５～１７：３０"],
            ["スクリーン０３", "１６：１０～１８：２５"]
        ]
    },
    {
        "title": "ＳＴＡＮＤ　ＢＹ　ＭＥドラえもん２",
        "date": "２０２０年１２月２４日",
        "hour": "１１０分",
        "restricted": False,
        "vacant": "◎",
        "timetbl": [
            ["スクリーン０２", "０９：１５～１１：１５"],
            ["スクリーン０６", "１１：４５～１３：３５"],
            ["スクリーン０５", "１４：５５～１６：４５"],
            ["スクリーン０６", "１９：２０～２１：１０"]
        ]
    },
    {
        "title": "劇場版「鬼滅の刃」無限列車編",
        "date": "２０２０年１２月２４日",
        "hour": "１１０分",
        "restricted": "ＰＧ１２",
        "vacant": "✕",
        "timetbl": [
            ["スクリーン０８", "０９：４０～１１：５５"],
            ["スクリーン０４", "１１：４０～１３：５０"],
            ["スクリーン０８", "１２：１５～１４：２５"],
            ["スクリーン０３", "１３：３５～１５：４５"],
            ["スクリーン０８", "１５：００～１７：１０"]
        ]
    },
    {
        "title": "映画　えんとつ町のプペル",
        "date": "２０２０年１２月２４日",
        "hour": "１１５分",
        "restricted": False,
        "vacant": "◎",
        "timetbl": [
            ["スクリーン０６", "０８：５０～１０：４５"],
            ["スクリーン０６", "１１：１０～１３：０５"],
            ["スクリーン０６", "１３：３０～１５：２５"],
            ["スクリーン０６", "１５：５０～１７：４５"],
            ["スクリーン０６", "１８：１０～２０：０５"]
        ]
    },
    {
        "title": "劇場版　ポケットモンスター　ココ",
        "date": "２０２０年１２月２４日",
        "hour": "１１５分",
        "restricted": False,
        "vacant": "◎",
        "timetbl": [
            ["スクリーン０７", "０８：３５～１０：３０"],
            ["スクリーン０８", "１０：０５～１２：００"],
            ["スクリーン０７", "１０：５５～１２：５０"],
            ["スクリーン０８", "１２：２５～１４：２０"],
            ["スクリーン０７", "１３：２０～１５：１５"]
        ]
    },
    {
        "title": "吹替　ワンダーウーマン　１９８４",
        "date": "２０２０年１２月２４日",
        "hour": "１６５分",
        "restricted": False,
        "vacant": "◎",
        "timetbl": [
            ["スクリーン０２", "０８：２０～１１：０５"],
            ["スクリーン０２", "１８：１５～２１：００"]
        ]
    },
    {
        "title": "パウ・パトロール　カーレース大作戦ＧＯ！ＧＯ！",
        "date": "２０２０年１２月２４日",
        "hour": "５５分",
        "restricted": False,
        "vacant": "◎",
        "timetbl": [
            ["スクリーン０３", "０９：３５～１０：３０"],
            ["スクリーン０７", "１５：１０～１６：０５"]
        ]
    }
]

#   初期設定
# [True]IPUTメンバー会員  [False]IPUTメンバー会員でない
iput_member = True
# この映画館での鑑賞回数
count = 5


# 画面クリア
console_clear_st = True
try:
    from google.colab import output
except ImportError:
    console_clear_st = False
    import os

def console_clear():
    if console_clear_st:
        output.clear()
    else:
        os.system("cls")



input("ようこそ！")
console_clear()
while True:
    gen = input("性別を選択してください \n1.男性 2.女性\n>")
    console_clear()
    age = input("年齢を入力してください>") # 下の入力欄に年齢を入力してください
    console_clear()
    if gen == "1":
        gen_p = "男性"
    if gen == "2":
        gen_p = "女性"
    res = input(f"この内容で正しいですか\n性別：{gen_p}  年齢：{age}\nやり直す n  /  はい y>")
    console_clear()
    if res == "y": break
movie_max = 3 # 一画面に表示するタイトル数
while True:
    for i in range(len(mdata)):
        if i < movie_max and i >= movie_max-3:
            print(f"{i+1}. {mdata[i]['title']}  時間：{mdata[i]['hour']}  {mdata[i]['restricted']}")
    mv_n = input("\n選択するには映画の番号を入力してください\n次のページ n  /  前のページ b\n>") # 選択するには映画の番号を入力してください
    console_clear()
    if mv_n == "n":
        movie_max += 3
        continue
    if mv_n == "b":
        movie_max -= 3
        continue
    movie_index = int(mv_n)-1
    break

