def ShiftNaive(a, n):
    tmp = a[0]
    counter = 1
    while counter <= len(a):
        if counter * n < len(a):
            tmp2 = a[counter * n]
            a[counter * n] = tmp
            tmp = tmp2
            counter += 1
        else:
            tmp2 = a[(counter * n)%len(a)]
            a[(counter * n)%len(a)] = tmp
            tmp = tmp2
            counter += 1
    return(a)


#Если gcd == 1:
a = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3
print(ShiftNaive(a, n))
#Алгоритм работает полноценно.

#Если gcd != 1:
a = [1, 2, 3, 4, 5, 6, 7, 8]
n = 4
print(ShiftNaive(a, n))
#Не все значения сдвинуты. Алгоритм замыкается в цикл, затрагивающий не все позиции списка, в результате чего в данном
# примере tmp принимает поочередно значения 1 и 5, меняя их местами до тех пор, пока счетчик не прервет цикл.