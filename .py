class Screen:
    L = []
    BD = [0,
        ["┏","┓","┗","┛","━","┃","┃"],     # Google Colaboratory
        ["┏━","━┓","┗━","━┛","━━","┃ "," ┃"] # Windows, Linux
    ]
    def SETTING(self, width=50, height=5, os=1):  # width - スクリーン横幅
        self.width = width              # os   - 1 Google Colaboratory, 2 Windows Linux
        self.os = os
        BD = self.BD
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
        title_len = len(title)
        b_len = int((width - title_len) / 2)
        for i in range(width):
            x = i - b_len - 1

            if i != 0 and i != width-1:   # ここ消してもいいかも
                self.L[0][i] = BD[os][4]
            if i == b_len:
                self.L[0][i] = BD[os][5]
            if i == b_len + title_len + 1:
                self.L[0][i] = BD[os][6]
            if i > b_len and x < title_len:
                self.L[0][i] = title[x]
    
    def WINDOW(self): # 出力
        for line in self.L:
            for raw in line:
                print(raw, end="")
            print()


s = Screen()
#   width=50 スクリーンの横幅
#   height=5 スクリーンの高さ
#   os=1 [Google Colaboratory],  os=2 [Windows] [Linux]
s.SETTING(width=50, height=20, os=2)
#   タイトルをセット (全角)
s.SET_TITLE("劇場版　ポケットモンスター　ココ")
#   出力
s.WINDOW()