N = int(input())

dig = [int(N) for N in str(N)]

count = 0

for i in range(1, len(dig)+1):
    if i != len(dig):
        count += i * 9 * (10**(i-1))

    else:
        count += i * (N - 10**(i-1) + 1)
        
print(count)