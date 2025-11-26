def combination_backtracking(nums, start, comb, k):
    if len(comb) == 6:
        print(' '.join(map(str, comb)))
        return
    
    for i in range(start, k):
        comb.append(nums[i])
        combination_backtracking(nums, i + 1, comb, k)
        comb.pop()

while(True):
    Row = list(map(int, input().split()))
    
    if Row==[0]:
        break
    
    k = Row.pop(0)
    combination_backtracking(Row, 0, [], k)
    print()
