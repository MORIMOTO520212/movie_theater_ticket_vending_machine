import re

text = "A011"
pattern = r"([A-Z]{1})([0-9]{2})"
res = re.match(pattern, text)

print(res.group())