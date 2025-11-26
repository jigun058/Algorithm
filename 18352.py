from collections import deque

N, M, K, X = map(int, input().split())

edges = {i : [] for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)

whenVisited = [-1] * (N+1)
queue = deque()
whenVisited[X] = 0
queue.append(X)

while(queue):
    current = queue.popleft()

    for next in edges[current]:
        if whenVisited[next] == -1:
            whenVisited[next] = whenVisited[current] + 1
            queue.append(next)

indices = []

for idx, val in enumerate(whenVisited):
    if val == K:
        indices.append(idx)
indices.sort()

if indices:
    for index in indices:
        print(index)
else:
    print(-1)