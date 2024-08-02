T = int(input())

a = [1,2,4]
for i in range(4,12):
    a.append(a[i-4]+a[i-3]+a[i-2])

for _ in range(T):
    n = int(input())
    print(a[n-1])