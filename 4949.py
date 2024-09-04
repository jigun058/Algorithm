S, P = map(int, input().split())
str = input()
nums = list(map(int, input().split()))

count = 0

for i in range(S-P+1):
    A, C, G, T = 0, 0, 0, 0
    for j in range(P):
        if str[i+j] == "A":
            A += 1
        if str[i+j] == "C":
            C += 1
        if str[i+j] == "G":
            G += 1
        if str[i+j] == "T":
            T += 1

    if A >= nums[0] and C >= nums[1] and G >= nums[2] and T >= nums[3]:
        count += 1

print(count)