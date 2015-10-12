n, k = input().split(' ')
n = int(n)
k = int(k)
def fact(a):
    if a == 0:
        return 1
    else:
        return a*fact(a - 1)
def combinations(n, k):
    ncomb = fact(n)/(fact(k)*fact(n-k))
    return int(ncomb)
if k > n:
    print(0)
else:
    print(combinations(n, k))
