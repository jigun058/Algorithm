mat = []
for _ in range(5):
    mat.append(list(map(int, input().split())))
    
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

set = set()

def dfs(x, y, tmp, length):
    if length == 6:
        set.add(tmp)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 5 and nx >= 0 and ny < 5 and ny >= 0:
            tmp + str(mat[nx][ny])
            dfs(nx, ny, tmp + str(mat[nx][ny]), length+1)

for x in range(5):
    for y in range(5):
        dfs(x, y, str(mat[x][y]), 1)

print(len(set))