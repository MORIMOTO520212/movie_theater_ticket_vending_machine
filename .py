import re

def re_uni_txt(text):
    pattern = r".*?(\033\[.*?m).*" # color script
    result = re.match(pattern, text)
    uni_txt = []
    if result:
        dec = result.group(1)
        res = text.split(dec)
        if "" != res[0]:
            for m in res[0]:
                uni_txt.append(m)
        res_2 = res[1].replace("\033[00m", " ")
        uni_txt.append(dec + res_2[0]) # '\033[??mあ'
        i = 0
        while i in range(len(res_2)):
            if " " == res_2[i]:
                uni_txt.append("")
            elif res_2[i] != res_2[0]:
                uni_txt.append(res_2[i])
            i += 1
        return uni_txt
    return 0

def re_uni_txt2(text):
    pattern = r".*?(\033\[.*?m).*" # color script
    result = re.match(pattern, text)
    uni_txt = []
    if result:
        dec = result.group(1)
        text = text.replace(dec, "@").replace("\033[00m", "#")
        i = 0
        #f = False
        while i < len(text):
            uni_txt.append(text[i])
            if text[i] == "@":
                if i:
                    uni_txt[i-1] += dec
                    uni_txt.remove("@")
                else:
                    uni_txt[i] = dec + text[i+1]
                    #f = True
                    i += 1
            elif text[i] == "#":
                uni_txt[i-2] += "\033[00m"
            i += 1
        try:
            uni_txt.remove("#")
        except: pass
        return uni_txt
    return text

A = "あいうえお"
B = ""

print(re_uni_txt2(A))

