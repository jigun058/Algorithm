N = int(input())

dp = [-1, 0, 1, 1, 2, 3, 2, 3, 3]

i = 9

while i <= N:
    if i%3 == 0 and i%2 == 0:
        num = min(dp[i//3], dp[i//2], dp[i-1]) + 1
    elif i%3 == 0:
        num = min(dp[i//3], dp[i-1]) + 1
    elif i%2 == 0:
        num = min(dp[i//2], dp[i-1]) + 1
    else:
        num = dp[i-1] + 1
    
    dp.append(num)
    i += 1


print(dp[N])