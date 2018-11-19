def fac(n):
    r = 1
    for i in range(2, n+1):
        r *= i
    return r

print(fac(50))