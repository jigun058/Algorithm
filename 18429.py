N, K = map(int, input().split())
up = list(map(int, input().split()))
up.insert(0, -1)
count = 0

def backtrack(path, options, result):
    if not options:
        result.append(path)
        return
    for i in range(len(options)):
        backtrack(path + [options[i]], options[:i] + options[i+1:], result)

def permute(nums):
    result = []
    backtrack([], nums, result)
    return result

nums = list(range(1, N+1))

for case in permute(nums):
    isFail = 0
    weight = 0

    for i in case:
        weight += up[i]
        weight -= K
        if(weight < 0):
            isFail = 1
            break
    
    if(isFail == 0):
        count += 1
    
print(count)