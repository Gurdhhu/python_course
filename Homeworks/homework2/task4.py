numbers = list(input().split(' '))
ints = []
for i in numbers:
    ints.append(int(i))
def rpfilter(a, *args):
    filtered = []
    def euclid(a, b):
        n, m = a, b
        if a < b:
            n, m = b, a
        if n % m == 0:
            return m
        else:
            return euclid(m, n % m)
    for i in args:
        if euclid(a, i) == 1:
            filtered.append(i)
    return filtered
result = rpfilter(*ints)
if result == []:
    print('None')
else:
    for i in result:
        print(i, end=' ')
