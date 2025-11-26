N = int(input())
km = list(map(int, input().split()))
won = list(map(int, input().split()))

sum = 0
good = [0]*N
good[0] = won[0]
kms = 0

for i in range(1, N):
    if(good[i-1] > won[i]):
        kms += km[i-1]
        sum += good[i-1]*kms
        kms = 0
        good[i] = won[i]
    elif(i==N-1):
        kms += km[i-1]
        sum += good[i-1]*kms
    else:
        good[i] = good[i-1]
        kms += km[i-1]

print(sum)