S, P = map(int, input().split())
str = input()
nums = list(map(int, input().split()))

count = 0

A, C, G, T = 0, 0, 0, 0

for j in range(P):
    if str[j] == "A":
        A += 1
    if str[j] == "C":
        C += 1
    if str[j] == "G":
        G += 1
    if str[j] == "T":
        T += 1

if A >= nums[0] and C >= nums[1] and G >= nums[2] and T >= nums[3]:
    count += 1

for i in range(1, S-P+1):
    if str[i-1] == 'A':
        A -= 1
    if str[i-1] == 'C':
        C -= 1
    if str[i-1] == 'G':
        G -= 1
    if str[i-1] == 'T':
        T -= 1

    if str[i+P-1] == "A":
        A += 1
    if str[i+P-1] == "C":
        C += 1
    if str[i+P-1] == "G":
        G += 1
    if str[i+P-1] == "T":
        T += 1
    
    if A >= nums[0] and C >= nums[1] and G >= nums[2] and T >= nums[3]:
        count += 1

print(count)
