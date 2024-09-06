N, M = map(int, input().split())
nums = list(map(int, input().split()))

def backtrack(start, path, result):
    if len(path) == M:
        result.append(tuple(path))
        return
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(i, path, result)
        path.pop()

def permute(nums):
    nums.sort()
    result = []
    backtrack(0, [], result)
    return result

ans = permute(nums)

bb = sorted(set(ans))

for com in bb:
    print(' '.join(map(str, com)))
