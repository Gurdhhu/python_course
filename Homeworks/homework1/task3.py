raw_input = input()
numbers = raw_input.split(' ')
sum = 0
for i in numbers:
    sum += int(i)
mean = sum/len(numbers)
print (mean)