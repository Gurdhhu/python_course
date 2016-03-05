n = int(input())
inheritance = {}
for i in range(n):
    child, *parents = input().split(" : ")
    if parents != []:
        parents = parents[0].split(" ")
    if child not in inheritance:
        inheritance[child] = {"class": parents}
    else:
        inheritance[child]["class"].append(parents)


def check(x, y):
    if x in inheritance:
        if y in inheritance[x]["func"]:
            return x
        else:
            for i in inheritance[x]["class"]:
                return check(i, y)


m = int(input())
for i in range(m):
    child, func = input().split(" ")
    if "func" not in inheritance[child]:
        inheritance[child]["func"] = [func]
    else:
        inheritance[child]["func"].append(func)

x, y = input().split(" ")
print(check(x, y))
