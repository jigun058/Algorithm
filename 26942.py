n = int(input())

stu = []
for i in range(n):
    stu.append(input())

m = int(input())

pair = []
for i in range(m):
    pair.append(list(map(stu.index,input().split())))

for i in range(n):
    stu[i] = i

graph = {i: [] for i in range(0, n)}

for n1, n2 in pair:
    graph[n1].append(n2)
    graph[n2].append(n1)

group = [[i, 0] for i in range(n)]

for i in range(n):
    if(group[i][1] == 1):
        continue
    stack = [i]

    while stack:
        temp = stack.pop()
        if(group[temp][1] == 0):
            group[temp][1] = 1
            for j in graph[temp]:
                if group[j][0] != group[temp][0]:
                    group[j][0] = group[temp][0]
                    stack.append(j)

gg = []
for i in range(n):
    gg.append(group[i][0])

print(len(set(gg)))