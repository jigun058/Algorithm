n, m = map(int, input().split())
a = list(map(int,input().split()))

for i in range(m):
    a.sort()
    sum = a[0] + a[1]
    a[0] = sum
    a[1] = sum

sum = 0
for i in range(n):
    sum += a[i]

print(sum)