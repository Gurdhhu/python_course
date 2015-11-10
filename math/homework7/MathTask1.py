a = [1, 5, 12, 11]
b = 7

def GeneClosest(a, b):
    closest = [a[0], abs(a[0] - b)]
    for i in a:
        if abs(i - b) < closest[1]:
            closest = [i, abs(i - b)]
    return(closest[0])

print(GeneClosest(a, b))