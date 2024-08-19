N, M = map(int, input().split())

edges = []

for i in range(M):
    edges.append(list(map(int, input().split())))
    
graph = {i: [] for i in range(1, N+1)}

for n1, n2, n3 in edges:
    graph[n1].append((n2, n3))

def reset():
    isVisited = [0]*(N+1)
    isVisited[0] = -1
    global max
    max = 0

maxRoute = []
maxnum = 0

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph):
        min_distance = float('inf')
        min_node = None
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        visited.add(min_node)

        for neighbor, weight in graph[min_node].items():
            if neighbor not in visited:
                new_distance = distances[min_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances

for i in graph:
    






# if maxRoute == []:
#     print("-1")

# else:
#     print(maxnum)
#     for i in maxRoute:
#         print(i, end=" ")
