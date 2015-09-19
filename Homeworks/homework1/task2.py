thing = input()
number = input()
two = ['2', '3', '4']
teens = ['11']
x=11
for i in range(7):
    x+=1
    teens.append(str(x))
if thing == 'ложка':
    if number[-1] == '1':
        if number[-2:] in teens:
            print (number, 'ложек')
        else:
            print (number, 'ложка')
    elif number[-2:] in teens:
        print (number, 'ложек')
    elif number[-1:] == '0':
        print (number, 'ложек')
    elif number[-1:] in two:
        print (number, 'ложки')
    else:
        print (number, 'ложек')
else:
    if number[-1] == '1':
        if number[-2:] in teens:
            print (number, 'утюгов')
        else:
            print (number, 'утюг')
    elif number[-2:] in teens:
        print (number, 'утюгов')
    elif number[-1:] == '0':
        print (number, 'утюгов')
    elif number[-1:] in two:
        print (number, 'утюга')
    else:
        print (number, 'утюгов')
