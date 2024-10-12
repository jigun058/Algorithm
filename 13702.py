N, K = map(int, input().split())

cap = []
for i in range(N):
    cap.append(int(input()))
    
cap.sort()

last = cap[0]
mid = last // 2
first = 0

def test(A):
    num = 0
    for i in cap:
        num += (i//A)
    return num

for _ in range(50):
    if test(mid) < K:
        last = mid
        mid = (first + last) // 2
    elif test(mid) > K:
        first = mid
        mid = (first + last) // 2
    else:
        while test(mid) == K:
            
            first = mid
            mid = (first + last) // 2
            
        break

print(mid)