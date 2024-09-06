N = int(input())

files = []
nums = {}

for i in range(N):
    asdf = list(input().split('.'))
    
    if asdf[1] not in nums:
        nums[asdf[1]] = 1
    else:
        temp = nums[asdf[1]]
        del nums[asdf[1]]
        nums[asdf[1]] = temp+1

sorted_dict = sorted(nums.items())

for i in sorted_dict:
    print(i[0] + " " + str(i[1]))