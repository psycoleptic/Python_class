#Напишите программу, которая спрашивает е пользователя как много чисел Фибоначчи
#  нужно сгенерировать а затем генерирует их

n = int(input("Сколько чисел Фибоначчи сгенерировать? "))
k = []
n0 = 0
n1 = 1
s = 0
while n1 <= n+1:
    tmp = n1 + n0
    n1 = n0 + n1
    n0 = tmp
    k.append(n1)
    s += n1
print(k)