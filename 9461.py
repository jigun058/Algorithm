dp = [0, 1, 1, 1, 2, 2]

T = int(input())
for _ in range(T):
    N = int(input())

    i = len(dp)
    while(i <= N):
        dp.append(dp[i-1] + dp[i-5])
        i += 1
    
    print(dp[N])