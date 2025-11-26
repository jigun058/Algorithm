N = int(input())

num = 9*(2**(N-1))
for i in range(N, -1, -1):
    num -= 2**(i-3)