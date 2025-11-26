dp = [0, 1, 2, 4]

T = int(input())
for _ in range(T):
    n = int(input())

    i = len(dp)
    while i <= n:
        dp.append((dp[i-1] + dp[i-2] + dp[i-3])%1000000009)

        i += 1


    print(dp[n])