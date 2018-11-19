#Напишите функцию, которая для заданного в аргументах списка, возвращает как результат перевернутый список

def revers(a, b):
    old_list = []
    for i in range(a, b):
        l = i+1
        old_list.append(l)
        i+= 3
    new_list = list(reversed(old_list))
    print(old_list)
    print(new_list)

a = int(input("Print a "))
b = int(input("Print b "))
print(revers(a, b))