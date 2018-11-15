x = int(input())
i = 2
m = 1
limit = int(x**0.5)
while i <= limit:
    if x % i == 0:
        m = m+1
        break
    i = i + 1
if m == 1:
    print("Prime number")
else:
    print("Composite number")