n = int(input())
numbers = []
while n > 0:
    numbers.append(int(input()))
    n -= 1
def prime(x):
    counter = 2
    while counter < x:
        if x % counter == 0:
            return 'False'
        else:
            counter += 1
    return 'True'
for i in numbers:
    print(prime(i))
