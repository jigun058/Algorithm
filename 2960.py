N, K = map(int, input().split())

nums = [i for i in range(2, N+1)]
count = 0
isEnd = 0

while count != K:
    div = nums[0]
    for i in nums:
        if i % div == 0:
            num = i
            nums.remove(i)
            count += 1
            if count == K:
                print(num)
                isEnd = 1
                break
    if isEnd:
        break
