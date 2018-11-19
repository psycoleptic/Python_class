#Напишите функцию, которая для заданного параметров интервала, выводит значение, некоторой математической функции
# (например: sin, cos ... для этого не забудьте подключить модуль math import math)

import math

def strange(a, b):
    for x in range(a, b):
        print(round(math.sin(x), 2))
        x +=1

a = int(input("Print a "))
b = int(input("Print b "))
print(strange(a, b))

