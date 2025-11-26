N, M = map(int, input().split())

matA = []
matB = []

for i in range(N):
    matA.append(list(map(int,input().split())))
    
for i in range(N):
    matB.append(list(map(int,input().split())))
    
for i in range(N):
    for j in range(M):
        print(matA[i][j] + matB[i][j], end=" ")
    print()

