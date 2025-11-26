T = int(input())
graph = {}

for i in range(1, T):
    num = int(input())
    graph[i] = list(map(int, input().split()))

def find_paths(current, path, visited, all_paths):
    if current == T:
        all_paths.append(path.copy())
        return
    for neighbor in graph.get(current, []):
        if not visited[neighbor]:
            visited[neighbor] = True
            path.append(neighbor)
            find_paths(neighbor, path, visited, all_paths)
            path.pop()
            visited[neighbor] = False

visited = [False] * (T + 1)
all_paths = []
current_path = [1]

visited[1] = True
find_paths(1, current_path, visited, all_paths)
cycle = 0

for path in all_paths:
    if(len(set(path)) != len(path)):
        cycle = 1
    
if(cycle == 1):
    print("CYCLE")
else:
    print("NO CYCLE")