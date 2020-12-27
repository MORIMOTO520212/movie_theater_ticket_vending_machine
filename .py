import re


def re_uni_txt(text):
    pattern = r".*?(\033\[.*?m).*" # fg
    result = re.match(pattern, text)
    uni_txt = []
    if result:
        fg = result.group(1)
        uni_txt.append(fg + text[len(fg)])
        for i in range(len(text)):
            if i == len(text)-6:
                uni_txt.append(text[i] +"\033[00m")
                break
            elif i > len(fg):
                uni_txt.append(text[i])
        return uni_txt
    return text


text = 'あいうえお'
text = re_uni_txt(text)
for m in text:
    print(m, end="")