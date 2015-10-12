a, b = input().split(' ')
a, b = int(a), int(b)
def euclid(a, b):
    n, m = a, b
    if a < b:
        n, m = b, a
    if n % m == 0:
        return m
    else:
        return euclid(m, n % m)
print(euclid(a, b))
