import re
import sys


text = sys.stdin.readlines()
pattern = "\W+"

out = ''
for i in range(len(text)):
    line = text[i]
    if i == len(text) - 1:
        line = re.sub('\W+$', '', line)
    out += re.sub('\W+', ' ', line)

print(out)