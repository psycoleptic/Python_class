# Напишите функцию вычисляющую N-ое число арифметической последовательности в рекурсивной форме

def rec_arifm(n, a0, d):
    n >= 2
    return a0 + (n - 1)*d
n = int(input("Print n = "))
d = int(input("Print d = "))
a0 = int(input("Print a1 = "))
print(rec_arifm(n, a0, d))