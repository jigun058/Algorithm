N, L, W, H = map(int, input().split())

last = min(L, W, H)
mid = round(last / 2, 11)

def test(A):
    return ((L//A) * (W//A) * (H//A))

if test(last) >= N:
    print(last)

else:    
    while test(mid) < N:
        if test(mid) < N:
            last = mid
            mid = round(last / 2, 11)

    first = mid
    mid = round((first + last) / 2, 11)
    for _ in range(100):
        if test(mid) < N:
            last = mid
            mid = round((first + last) / 2, 11)
        else:
            first = mid
            mid = round((first + last) / 2, 11)

    print(mid)