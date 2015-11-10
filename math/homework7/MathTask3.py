a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def PartialSum(a):
    for i in range(len(a) - 1):
        a[i + 1] = a[i] + a[i + 1]
    return(a)

print(PartialSum(a))