import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    
    for i in range(3, n):
        count=0
        for j in range(2, int(i**(1/2))+1):
            if i%j == 0:
                count += 1
                break
        if count == 0:
            for j in range(2, int((n-i)**(1/2))+1):
                if ((n-i)%j == 0):
                    count += 1
                    break
            if count == 0:
                print(n, "=", i, "+", n-i)
                break