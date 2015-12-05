import re

with open("hp5.txt", "r") as f:
    text = f.read()

pattern = "whisper\w* ([A-Z]\w+( [A-Z]\w+)*)|([A-Z]\w+( [A-Z]\w+)*) whisper\w*"
whisperers = re.findall(pattern, text)
print(whisperers)
namelib = {}
for match in whisperers:
    tmp = ''
    for name in match:
        if len(tmp) < len(name):
            tmp = name
    if tmp not in namelib:
        namelib[tmp] = 1
    else:
        namelib[tmp] += 1

result = (0, '')
for i in namelib:
    if result[0] < namelib[i]:
        result = (namelib[i], i)

print(result[0], result[1])