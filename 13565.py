from collections import deque
m, n = map(int, input().split())

mat = []
for _ in range(m):
    mat.append(list(map(int, input())))

queue = deque()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i):
    if mat[0][i] == 0:
        queue.append([0, i])

        while(queue):
            here = queue.popleft()
            mat[here[0]][here[1]] = 1

            for j in range(4):
                next = [here[0] + dx[j], here[1] + dy[j]]
                if 0 <= next[0] < m and 0 <= next[1] < n:
                    if mat[next[0]][next[1]] == 0:
                        if next[0] == m-1:
                            return 1
                        
                        queue.append(next)
                        mat[next[0]][next[1]] = 1

    
    return 0

for i in range(n):
    if bfs(i) == 1:
        print("YES")
        break
    elif i == n-1:
        print("NO")
    else:
        continue