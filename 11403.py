N = int(input())

mat = []
for _ in range(N):
    line = list(map(int, input().split()))
    for i in range(N):
        if line[i] == 0:
            line[i] = float("inf")

    mat.append(line)
    
for m in range(N):
    for i in range(N):
        for j in range(N):
            mat[i][j] = min(mat[i][j], mat[i][m] + mat[m][j])

for i in range(N):
    for j in range(N):
        if mat[i][j] == float("inf"):
            print('0', end = " ")
        else:
            print('1', end = " ")
    print()