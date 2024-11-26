from collections import deque

N = int(input())
stones = [0]
stones.extend(list(map(int, input().split())))
a, b = map(int, input().split())

whenVisited = [-1] * (N+1)

queue = deque()

def bfs(a):
    if N == 1:
        return 0

    whenVisited[a] = 0
    queue.append(a)

    while(queue):
        here = queue.popleft()

        for i in range(1, N):
            jump = stones[here]*i
            next = here + jump

            if next > N:
                break
            elif whenVisited[next] > (whenVisited[here] + 1) or whenVisited[next] == -1:
                whenVisited[next] = whenVisited[here] + 1
                queue.append(next)

                if next == b:
                    return whenVisited[next]
    
    return -1

print(bfs(a))