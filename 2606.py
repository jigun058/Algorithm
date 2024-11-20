from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
P = int(input())
lst = []
net = {i : [] for i in range(1, N+1)}

for _ in range(P):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

isVisited = [0]*(N+1)

queue = deque()
queue.append(1)

while queue:
    here = queue.popleft()
    isVisited[here] = 1

    for i in net[here]:
        if not isVisited[i]:
            queue.append(i)
        else:
            continue

print(isVisited.count(1) - 1)