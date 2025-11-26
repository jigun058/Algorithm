N, M = map(int, input().split())

friends = [([100] * N) for _ in range(N)]

for i in range(0, N):
    friends[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    friends[a-1][b-1] = 1
    friends[b-1][a-1] = 1
    
for k in range(N):
    for a in range(N):
        for b in range(N):
            friends[a][b] = min(friends[a][b], friends[a][k] + friends[k][b])

mins = [0, 1000000000]
for i in range(N):
    sum = 0
    for j in range(N):
        sum += friends[i][j]
    
    if sum < mins[1]:
        mins[0] = i
        mins[1] = sum

print(mins[0]+1)