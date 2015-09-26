raw_input = input()
numbers = raw_input.split(' ')
int_num = []
for i in numbers:
    int_num.append(int(i))
list1 = int_num[0::2]
list1.sort()
list2 = int_num[1::2]
list2.sort(reverse=True)
sorted_list = []
k = 0
for i in range(len(list1)):
    sorted_list.append(list1[i])
    sorted_list.append(list2[i])
for j in sorted_list:
    print(j, end=' ')
