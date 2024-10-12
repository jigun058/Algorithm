N = int(input())

in_order = [input() for _ in range(N)]
out_order = [input() for _ in range(N)]

count = 0

for i in range(N):
    for j in range(i):
        if out_order.index(in_order[i]) < out_order.index(in_order[j]):
            count += 1
            break
    
print(count)