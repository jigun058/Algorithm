N, M, R = map(int, input().split())
edges = []

for i in range(M):
    edges.append(list(map(int, input().split())))

depth = [-1] * (N + 1)
stack = [(R, 0)]

graph = {i: [] for i in range(1, N + 1)}

for n1, n2 in edges:
    graph[n1].append(n2)
    graph[n2].append(n1)

asdf = [0]*N
count = 1

while stack:
    node, dep = stack.pop()
    if depth[node] == -1:
        depth[node] = dep
        asdf[node-1] = count
        count += 1
        for neighbor in sorted(graph[node], reverse=True):
            if depth[neighbor] == -1:
                stack.append((neighbor, dep + 1))

for i in range(0, N):
    print(asdf[i])