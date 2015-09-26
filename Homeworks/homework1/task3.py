numbers = [int(x) for x in input.split(' ')]
sum = 0
for i in numbers:
    sum += i
mean = sum/len(numbers)
print(mean)
