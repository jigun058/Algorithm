# def find_div_sum(n):
#     sum = 0
    
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             sum += i
#             if i != n**0.5:
#                 sum += n // i

#     return sum

T = int(input())

for i in range(T):
    N = int(input())

    sum = N**2
    for j in range(1, N+1):
        sum -= j*(N//j) - N
    
    print(sum)