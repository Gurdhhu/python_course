n = int(input())
dic = {}
for i in range(n):
    offspr, *anc = input().split(" : ")
    if anc != []:
        anc = anc[0].split(" ")
    if offspr not in dic:
        dic[offspr] = anc
    else:
        dic[offspr].append(anc)

q = int(input())

requests = []
for i in range(q):
    requests.append(input())


def check(x):
    if x not in visited:
        visited.append(x)
        if x in dic:
            for i in dic[x]:
                check(i)
    else:
        return


for i in requests:
    visited = []
    anc, offspr = i.split(" ")
    check(offspr)
    if anc in visited:
        print("Yes")
    else:
        print("No")
