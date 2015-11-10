a = [1, 2, 2, 1, 1, 2]

def Major(a):
    elem = a[0]
    count = 1
    for i in range(1, len(a)):
        if a[i] == elem:
            count += 1
        else:
            count -= 1
            if count == -1:
                elem = a[i]
                count = 1
    count = 0
    for i in a:
        if i == elem:
            count += 1
    if len(a)/count < 2:
        return(elem)
    else:
        return(None)

print(Major(a))

#Алгоритм будет по-прежнему работать за О(n), так как он пробегает по массиву всего лишь два раза.
# К тому же он не будет потреблять дополнительной памяти.