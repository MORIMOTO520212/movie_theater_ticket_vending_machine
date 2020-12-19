#from google.colab import output  画面クリアモジュール
#output.clear() 画面クリア
#
#   映画館　券売機システム
#   created 2020.12.18
#   
#   流れ
#   1.年齢確認
#   2.年齢制限内の上映予定の映画一覧を表示
#       IPUTメンバー会員かつ鑑賞回数5回の場合チケット料金を一律1000円で表示
#       18歳～59歳まではチケット料金一律1800円で表示
#       60歳～はチケット料金一律1000円
#
#   [リファレンス]
#   bashで16色表示するスクリプト用意しておくと便利 (https://gist.github.com/soramugi/7968403)
#   イオンシネマズの券売機でチケットを購入してみた (https://www.youtube.com/watch?v=iMuR0ATD48g)
#   Google Colabの出力を定期的にクリアする方法 (https://www.366service.com/jp/qa/dfe7790f6cc709645fb160e50e504b22)

import os

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
    clear = False
    import os

def console_clear():
    if console_clear_st:
        output.clear()
        return 0
    os.system("cls")


from msvcrt import getch

# メインループ
while True:
    key = ord(getch())
    if key == 0:
        key = ord(getch())
        if key == ord('H'):
            print("上")
            continue
        elif key == ord('P'):
            print("下")
            continue
        elif key == ord('K'):
            print("左")
            continue
        elif key == ord('M'):
            print("右")
            continue
    elif key == 13:
        print("エンター")
    elif key == 3:
        print("CTRL + C")
    else:
        message = f'keydown {key}'
        print(message)