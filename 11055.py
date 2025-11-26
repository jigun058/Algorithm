# N = int(input())

# a = list(map(int, input().split()))
# a.append(1001)

# dp = [0]*(N)
# dp.append(1001)

# point = a[N-1]

# dp[N-1] = a[N-1] + 1001

# for i in range(N-2, -1, -1):
#     if a[i] < point:
#         dp[i] = dp[i+1] + a[i]
#         point = a[i]
        
#     else:
#         for j in range(i+1, N+1):
#             if a[i] < a[j]:
#                 if dp[j] + a[i] > dp[i+1]:
#                     dp[i] = dp[j] + a[i]
#                     point = a[i]
#                     break
#                 else:
#                     dp[i] = dp[i+1]
#                     break

# print(dp[0]-1001)


N = int(input())

a = list(map(int, input().split()))

dp = a[:]

for i in range(1, N):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + a[i])

print(max(dp))