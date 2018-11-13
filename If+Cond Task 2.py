x: int = int(input("Put x "))
y = int(input("Put y "))

for l in range(x, y + 1):
    i = 2
    m = 1
    limit = int(l ** 0.5)
    while i <= limit:
        if l % i == 0:
            m = m+1
            break
        i = i + 1
    if m == 1:
        print(l)
    continue
