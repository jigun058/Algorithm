def backtrack(path, options, result):
    if not options:
        result.append(path)
        return
    for i in range(len(options)):
        # 다음 순열 생성을 위해 현재 숫자를 선택
        backtrack(path + [options[i]], options[:i] + options[i+1:], result)

def permute(nums):
    result = []
    backtrack([], nums, result)
    return result

# 예시 실행: 1부터 N까지의 숫자에서 모든 순열 생성
N = 3
nums = list(range(1, N+1))
all_permutations = permute(nums)
print(all_permutations)