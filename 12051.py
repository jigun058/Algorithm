def calM(r, c, num):
    global matrix
    matrix[r][c] = num

def calQ():
    global matrix, R, C
    visited = [[False for _ in range(C)] for _ in range(R)]
    count = 0

    def dfs(r, c):
        stack = [(r, c)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while stack:
            cr, cc = stack.pop()
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    stack.append((nr, nc))

    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j)
                count += 1

    print(count)

T = int(input())

for i in range(1, T+1):
    R, C = map(int,input().split())
    matrix = []

    for _ in range(R):
        numstr = input()
        row = [int(a) for a in numstr]
        matrix.append(row)
    
    N = int(input())

    print("Case #" + str(i) + ":")
    for j in range(N):
        command = input()
        if(command == "Q"):
            calQ()
        else:
            m, r, c, num = command.split()
            r, c, num = map(int, (r, c, num))
            calM(r, c, num)
