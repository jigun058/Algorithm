from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())

    ver = []
    for _ in range(n+2):
        a, b = map(int, input().split())
        ver.append((a, b))

    adj = {i : [] for i in range(0, n+2)}
    for i in range(n+2):
        for j in range(n+2):
            dist = abs(ver[i][0] - ver[j][0]) + abs(ver[i][1] - ver[j][1])
            if i != j and dist <= 1000:
                adj[i].append(j)

    isVisited = [0] * (n+2)

    def bfs(start):
        queue = deque()
        queue.append(start)
        isVisited[start] = 1

        while(queue):
            here = queue.popleft()
            for ad in adj[here]:
                if isVisited[ad] == 0:
                    isVisited[ad] = 1
                    queue.append(ad)

                    if ad == n+1:
                        return 1
        return 0
        
    result = bfs(0)
    if result:
        print("happy")
    else:
        print("sad")
