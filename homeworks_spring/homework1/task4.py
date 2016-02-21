length = int(input())
stack = input().split()
exnum = int(input())
exlist = []
for i in range(exnum):
    exlist.append(input())
cur_ex = input()
exlib = {}

for i in exlist:
    if i.split()[0] not in exlib:
        exlib[i.split()[0]] = {i.split()[1]: i.split()[2]}
    else:
        exlib[i.split()[0]][i.split()[1]] = i.split()[2]

for fun in reversed(stack):
    if cur_ex in exlib[fun]:
        if exlib[fun][cur_ex] == '_':
            break
        else:
            cur_ex = exlib[fun][cur_ex]
            length -= 1
    else:
        length -= 1

print(" ".join(stack[:length]))
