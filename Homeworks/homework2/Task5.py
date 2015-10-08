numbers = list(input().split(' '))
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
        if euclid(int(a), int(i)) == 1:
            filtered.append(i)
    return filtered
result = rpfilter(*numbers)
if result == []:
    print('None')
else:
    print(' '.join(result))
