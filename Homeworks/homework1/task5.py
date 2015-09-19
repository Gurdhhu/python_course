string = input()
sorted_str = []
for i in string:
    sorted_str.append(i)
sorted_str.sort()
total = 0
while total < len(sorted_str):
    print (sorted_str[total], sorted_str.count(sorted_str[total]))
    total += sorted_str.count(sorted_str[total])