from collections import deque

V, E = map(int, input().split())

group = [0]*(V+1)
adj = {i : [] for i in range(1, V+1)}

for i in range(E):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

queue = deque()
gr = 0

for i in range(1, V+1):
    if group[i] != 0:
        continue

    gr += 1
    queue.append(i)
    group[i] = gr
    while queue:
        here = queue.popleft()
        
        for j in adj[here]:
            if group[j] == 0:
                queue.append(j)
                group[j] = gr

print(gr)