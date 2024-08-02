N, K = map(int, input().split())
A = []
count = 0

for _ in range(N):
    A.append(int(input()))

while(K != 0):
    for i in range(N-1, -1, -1):
        if(K < A[i]):
            continue
        else:
            K -= A[i]
            count += 1
            break

print(count)