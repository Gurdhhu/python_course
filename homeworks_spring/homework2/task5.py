dic = {}
processing = []

n = int(input())
for i in range(n):
    x, *y = input().split(" : ")
    if y != []:
        y = y[0].split(" ")
    dic[x] = y

m = int(input())
for i in range(m):
    processing.append(input())


def check(x):
    if x not in visited:
        visited.append(x)
        if x in dic:
            for i in dic[x]:
                check(i)
    else:
        return


c = 0
for i in processing:
    visited = []
    check(i)
    for j in visited:
        if j in processing[:c]:
            print(i)
            break
    c += 1
