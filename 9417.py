N = int(input())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

for _ in range(N):
    nums = list(map(int, input().split()))
    max = 0

    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]>nums[j]:
                a, b = nums[i], nums[j]
            else:
                a, b = nums[j], nums[i]

            asdf = gcd(a, b)
            if max<asdf:
                max = asdf
    
    print(max)