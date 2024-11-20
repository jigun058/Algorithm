from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))

queue = deque()
queue.append([0, 0])

isEnd = False

while queue:
    here = queue.popleft()
    if mat[here[0]][here[1]] == -1:
        print("HaruHaru")
        isEnd = True
        break

    if mat[here[0]][here[1]] == 0:
        continue

    n = mat[here[0]][here[1]]

    if here[1] + n < N:
        next = [here[0], here[1] + n]
        queue.append(next)
    
    if here[0] + n < N:
        next = [here[0] + n, here[1]]
        queue.append(next)

if not isEnd:
    print("Hing")