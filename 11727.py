N = int(input())

k = [0, 1, 3, 5]

if(N<=3):
    print(k[N])
else:
    for i in range(4, N+1):
        k.append(k[i-1]+2*k[i-2])

    print(k[N]%10007)
    한글 =