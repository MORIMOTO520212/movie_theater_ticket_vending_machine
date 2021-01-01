EXAMPLEmdata = [
    {
        "title": "約束のネバーランド",
        "date": "２０２０年１２月２４日",
        "hour": "１３５分",
        "restricted": False,
        "timetbl": [
            ["スクリーン０１", "０９：４５～１２：００", "slight"],
            ["スクリーン０３", "１０：５５～１３：１０", "empty"],
            ["スクリーン０１", "１２：２５～１４：４０", "slight"],
            ["スクリーン０１", "１５：１５～１７：３０", "slight"],
            ["スクリーン０３", "１６：１０～１８：２５", "full"]
        ]
    },
    {
        "title": "ＳＴＡＮＤ　ＢＹ　ＭＥドラえもん２",
        "date": "２０２０年１２月２４日",
        "hour": "１１０分",
        "restricted": False,
        "timetbl": [
            ["スクリーン０２", "０９：１５～１１：１５", "◎"],
            ["スクリーン０６", "１１：４５～１３：３５", "◎"],
            ["スクリーン０５", "１４：５５～１６：４５", "◎"],
            ["スクリーン０６", "１９：２０～２１：１０", "◎"]
        ]
    },
    {
        "title": "劇場版「鬼滅の刃」無限列車編",
        "date": "２０２０年１２月２４日",
        "hour": "１１０分",
        "restricted": "ＰＧ１２",
        "timetbl": [
            ["スクリーン０８", "０９：４０～１１：５５", "✕"],
            ["スクリーン０４", "１１：４０～１３：５０", "✕"],
            ["スクリーン０８", "１２：１５～１４：２５", "✕"],
            ["スクリーン０３", "１３：３５～１５：４５", "△"],
            ["スクリーン０８", "１５：００～１７：１０", "✕"]
        ]
    },
    {
        "title": "映画　えんとつ町のプペル",
        "date": "２０２０年１２月２４日",
        "hour": "１１５分",
        "restricted": False,
        "timetbl": [
            ["スクリーン０６", "０８：５０～１０：４５", "◎"],
            ["スクリーン０６", "１１：１０～１３：０５", "△"],
            ["スクリーン０６", "１３：３０～１５：２５", "△"],
            ["スクリーン０６", "１５：５０～１７：４５", "◎"],
            ["スクリーン０６", "１８：１０～２０：０５", "△"]
        ]
    },
    {
        "title": "劇場版　ポケットモンスター　ココ",
        "date": "２０２０年１２月２４日",
        "hour": "１１５分",
        "restricted": False,
        "timetbl": [
            ["スクリーン０７", "０８：３５～１０：３０", "◎"],
            ["スクリーン０８", "１０：０５～１２：００", "△"],
            ["スクリーン０７", "１０：５５～１２：５０", "△"],
            ["スクリーン０８", "１２：２５～１４：２０", "△"],
            ["スクリーン０７", "１３：２０～１５：１５", "✕"]
        ]
    },
    {
        "title": "吹替　ワンダーウーマン　１９８４",
        "date": "２０２０年１２月２４日",
        "hour": "１６５分",
        "restricted": False,
        "timetbl": [
            ["スクリーン０２", "０８：２０～１１：０５", "◎"],
            ["スクリーン０２", "１８：１５～２１：００", "◎"]
        ]
    },
    {
        "title": "パウ・パトロール　カーレース大作戦ＧＯ！ＧＯ！",
        "date": "２０２０年１２月２４日",
        "hour": "５５分",
        "restricted": False,
        "timetbl": [
            ["スクリーン０３", "０９：３５～１０：３０", "◎"],
            ["スクリーン０７", "１５：１０～１６：０５", "◎"]
        ]
    }
]

import random, datetime

def toem(n):
    # 半角数字から全角数字に変換する
    num = ["０","１","２","３","４","５","６","７","８","９"]
    em = ""
    for i in str(n):
        em += num[int(i)]
    return em

# empty - 余裕あり
# slight - 残りわずか
# full - 満席

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

print(mdata)