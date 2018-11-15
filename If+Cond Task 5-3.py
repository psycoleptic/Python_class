n0 = 0
n1 = 1
s = 0
while n1 < 4000000:
    #tmp = n1 + n0
    #n1 = n0 + n1
    #n0 = tmp
    n1, n0 = n1+ n0, n1
    if n1%2 == 0:
        s += n1
print(s)