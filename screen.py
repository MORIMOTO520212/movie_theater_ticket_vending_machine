class Screen:
    L1 = ["  " for i in range(50)]
    L2 = ["  " for i in range(50)]
    L3 = ["  " for i in range(50)]
    L4 = ["  " for i in range(50)]
    L5 = ["  " for i in range(50)]
    BD = [0,
        ["┏","┓","┗","┛","━","┃","┃"],     # Google Colaboratory
        ["┏━","━┓","┗━","━┛","━━","┃ "," ┃"] # Windows, Linux
    ]
    def SETTING(self, width=50, os=1):  # width - スクリーン横幅
        self.width = width              # os   - 1 Google Colaboratory, 2 Windows Linux
        self.os = os
        BD = self.BD
        self.L1 = ["  " for i in range(width)]
        self.L2 = ["  " for i in range(width)]
        self.L3 = ["  " for i in range(width)]
        self.L4 = ["  " for i in range(width)]
        self.L5 = ["  " for i in range(width)]
        if os == 1:
            self.L1[0]       = BD[1][0]
            self.L1[width-1] = BD[1][1]
            self.L5[0]       = BD[1][2]
            self.L5[width-1] = BD[1][3]
            self.L2[0]           = BD[1][5]
            self.L2[width-1]     = BD[1][6]
            self.L3[0]           = BD[1][5]
            self.L3[width-1]     = BD[1][6]
            self.L4[0]           = BD[1][5]
            self.L4[width-1]     = BD[1][6]
        if os == 2:
            self.L1[0]       = BD[2][0]
            self.L1[width-1] = BD[2][1]
            self.L5[0]       = BD[2][2]
            self.L5[width-1] = BD[2][3]
            self.L2[0]           = BD[2][5]
            self.L2[width-1]     = BD[2][6]
            self.L3[0]           = BD[2][5]
            self.L3[width-1]     = BD[2][6]
            self.L4[0]           = BD[2][5]
            self.L4[width-1]     = BD[2][6]
        for i in range(width):
            if i != 0 and i != width-1:
                self.L1[i] = BD[os][4]
                self.L5[i] = BD[os][4]

    def SET_TITLE(self, title="ＮｏＴｉＴｌｅ"):
        width = self.width
        BD = self.BD
        os = self.os
        title_len = len(title)
        b_len = int((width - title_len) / 2)
        for i in range(width):
            x = i - b_len - 1

            if i != 0 and i != width-1:
                self.L1[i] = BD[os][4]
            if i == b_len:
                self.L1[i] = BD[os][5]
            if i == b_len + title_len + 1:
                self.L1[i] = BD[os][6]
            if i > b_len and x < title_len:
                self.L1[i] = title[x]
    
    def WINDOW(self):
        for raw in self.L1: print(raw, end="")
        print()
        for raw in self.L2: print(raw, end="")
        print()
        for raw in self.L3: print(raw, end="")
        print()
        for raw in self.L4: print(raw, end="")
        print()
        for raw in self.L5: print(raw, end="")
        print()



s = Screen()
#   width=50 スクリーンの横幅
#   os=1 [Google Colaboratory],  os=2 [Windows] [Linux]
s.SETTING(width=50, os=2)
#   タイトルをセット
s.SET_TITLE("劇場版ポケットモンスター　ココ")
#   出力
s.WINDOW()