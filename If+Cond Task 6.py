a = []
for n in range(0,1000):
    if n % 3 == 0 or n % 5 == 0:
        a.append(n)
print(sum(a))