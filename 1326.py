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

            next_forward = here + jump
            if next_forward <= N and (whenVisited[next_forward] == -1 or whenVisited[next_forward] > whenVisited[here] + 1):
                whenVisited[next_forward] = whenVisited[here] + 1
                queue.append(next_forward)
                if next_forward == b:
                    return whenVisited[next_forward]

            next_backward = here - jump
            if next_backward >= 1 and (whenVisited[next_backward] == -1 or whenVisited[next_backward] > whenVisited[here] + 1):
                whenVisited[next_backward] = whenVisited[here] + 1
                queue.append(next_backward)
                if next_backward == b:
                    return whenVisited[next_backward]
    
    return -1

print(bfs(a))