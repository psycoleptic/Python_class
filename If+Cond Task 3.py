x: int = int(input("Put x "))
y = int(input("Put y "))
n = input("Print 'true' or 'false' ")
if n == 'true':
    for l in range(x, y + 1):
        m = 1
        while y+1 >= l:
            if l % 2 == 0:
                m = m+1
                break
        if m == 1:
            print(l)

else:
    for l in range(x, y + 1):
        m = 1
        while y+1 >= l:
            if l % 2 != 0:
                m = m+1
                break
        if m == 1:
            print(l)
