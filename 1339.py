N = int(input())

dic = {}
max = 0
for _ in range(N):
    asdf = input()
    tmp = len(asdf)
    if(max < tmp):
        max = tmp

    for i in range(1, len(asdf)+1):
        dic[i].append(asdf[len(asdf)-i])

for i in range(max, 0, -1):
    if(len())