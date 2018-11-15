x = int(input("Print x "))
y = int(input("Print y "))
z = []
for a in range(x,y):
    for b in range(a, y):
        for c in range(b, y):
            if a**2 + b**2 == c**2:
                z.append(a)
                z.append(b)
                z.append(c)
                z.append(';')
print(z)