N, M = map(int, input().split())

notheard = set(input() for _ in range(N))
notseen = set(input() for _ in range(M))

asdf = sorted(notheard & notseen)

print(len(asdf))
for i in range(len(asdf)):
    print(asdf[i])