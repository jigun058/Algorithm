N = int(input())
A = list(map(int,input().split()))
oper = list(map(int,input().split()))
operations = [1]*oper[0] + [2]*oper[1] + [3]*oper[2] + [4]*oper[3]
max = -1111111111
min = 1111111111

def compute(A, operation):
    num = A[0]
    for i in range(N-1):
        if(operation[i] == 1):
            num += A[i+1]
        elif(operation[i] == 2):
            num -= A[i+1]
        elif(operation[i] == 3):
            num *= A[i+1]
        elif(operation[i] == 4):
            if(num<0):
                num = (-num)//A[i+1]*(-1)
            else:
                num = num//A[i+1]
    return num

def permutations(arr):
    if len(arr) == 0:
        return [[]]

    result = []

    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for perm in permutations(rest):
            result.append([arr[i]] + perm)

    return result

arr = permutations(operations)
for i in arr:
    num = compute(A, i)
    if(num<min):
        min = num
    if(num>max):
        max = num

print(max)
print(min)