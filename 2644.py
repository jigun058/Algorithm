from collections import deque

n = int(input())    #사람 수
a, b = map(int, input().split())    #a to b
m = int(input())    #관계 수

link = {i : [] for i in range(1, n+1)}
for _ in range(m):
    x, y = map(int, input().split())
    link[x].append(y)
    link[y].append(x)

whenVisited = [-1] * (n+1)
queue = deque()
whenVisited[a] = 0
queue.append(a)

def dfs(queue):
    while(queue):
        current = queue.popleft()

        for next in link[current]:
            if whenVisited[next] == -1:
                whenVisited[next] = whenVisited[current] + 1
                queue.append(next)

                if next == b:
                    return whenVisited[next]
    
    return -1
                
print(dfs(queue))