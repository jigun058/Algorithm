N, T = map(int, input().split())

time = []
for _ in range(N):
    s, i, c = map(int, input().split())

    if c == 1 and T <= s:
        time.append(s-T)
        continue
    if c == 1 and T > s:
        continue
    if T <= s:
        time.append(s-T)
        continue
    if T > s + (c-1)*i:
        continue
    
    num = [s + mul*i for mul in range(c)]
    first = 0
    last = c-1
    mid = (c-1)//2

    asdf = 0

    while(first+1 != last):
        if(T < num[mid]):
            last = mid
            mid = (first + last)//2
        elif(T > num[mid]):
            first = mid
            mid = (first + last)//2
        else:
            time.append(0)
            asdf = 1
            break
    
    if not asdf:
        time.append(num[last] - T)

if time:
    time.sort()
    print(time[0])
else:
    print("-1")