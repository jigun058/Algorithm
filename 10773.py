stack = []
K = int(input())


for _ in range(K):
    n = int(input())
    
    if n != 0:
        stack.append(n)
    else:
        stack.pop()
    
sum = 0
for i in stack:
    sum += i
print(sum)