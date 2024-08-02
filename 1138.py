N = int(input())
tall = list(map(int, input().split()))
table = [0]*N

for i in range(1, N+1):
    count = 0
    num = tall[i-1]

    for j in range(N):
        if(num == count and table[j] == 0):
            table[j] = i
            break
        elif(table[j] == 0):
            count += 1

for i in range(N):
    print(table[i], end=" ")