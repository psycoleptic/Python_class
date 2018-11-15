x = int(input())
y = int(input())
for i in range (x, y):
    while i <= limit:
        if x % i == 0:
            print()
            break
        i = i + 1
    print("Prime number")