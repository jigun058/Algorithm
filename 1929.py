nums = list(map(int, input().split()))

for i in range(nums[0],nums[1]+1) :
    count = 0
    for j in range(2, int(i**(1/2))+1) :
        if i%j == 0 :
            count += 1
            break
    if (count == 0) & (i != 1):
        print(i)
