N = int(input())

mul = 1

while N>0:
    mul *= N
    N -= 1
    
print(mul)