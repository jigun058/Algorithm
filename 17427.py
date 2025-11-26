t = int(input())

for j in range(t) :
    n = int(input())
    gN = 0
    for i in range(1, n+1) :
        gN += i * (n//i)
    print(gN)