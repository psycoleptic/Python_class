x: int = int(input("Put x "))
y = int(input("Put y "))
n = input("Print 'true' or 'false' ")
a = []
b = []
for l in range(x, y + 1):
    if l % 2 == 0:
        a.append(l)
    else:
        if l % 2 != 0:
            b.append(l)
if n == 'true':
    print(a)
else:
    print(b)