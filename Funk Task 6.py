#Напишите функцию вычисляющую N-ое число арифметической последовательности, шаг последовательности должен передаваться
#дополнительным аргументов (по умолчанию этот аргумент должен быть равен 1)

def arifm(n, d =1):
    a1 = 1
    an = 0
    i = 1
    while i <= n:
        an = a1 + (i-1)*d
        i += 1
    return an

n = int(input("Print n  "))
d = int(input("Print d  "))
print(arifm(n, d))