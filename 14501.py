N = int(input())

tp = []
for i in range(N):
    t, p = map(int, input().split())
    tp.append([t, p])

dp = [0]*N

i = N
while i > 0:
    if 