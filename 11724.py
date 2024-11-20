from collections import deque

V, E = map(int, input().split())

ver = [i for i in range(1, V)]
group = [0]*(V+1)
adj = {i : [] for i in range(1, V+1)}

for i in range(E):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

queue = deque()
gr = 0

if V==1:
    print(1)

else:
    while ver:
        gr += 1
        queue.append(ver[0])
        
        while queue:
            here = queue.popleft()
            if group[here] == 0:
                group[here] = gr
                if here in ver:
                    ver.remove(here)
            
            for i in adj[here]:
                if group[i] == 0:
                    queue.append(i)

    print(gr)