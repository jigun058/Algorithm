n = int(input())
pre = []
for i in range(n):
    asdf = list(input().split())
    pre.append(tuple([asdf[0], asdf[2]]))

m = int(input())
con = []
for i in range(m):
    asdf = list(input().split())
    con.append(tuple([asdf[0], asdf[2]]))

graph = {i: j for i, j in pre}

def dfs(start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    next_node = graph.get(start)
    if next_node and next_node not in visited:
        dfs(next_node, visited)
    return visited

for (i, j) in con:
    visited = dfs(i)
    if j in visited:
        print('T')
    else:
        print('F')