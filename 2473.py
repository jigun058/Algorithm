N = int(input())
vals = list(map(int,input().split()))

vals.sort()
result = []

min = 3000000001

for i in range(len(vals)-2):

    start = i+1
    end = len(vals)-1

    while start < end:
        sum = vals[i] + vals[start] + vals[end]
        a_sum = abs(sum)

        if a_sum < min:
            min = a_sum
            result = [vals[i], vals[start], vals[end], min]

        if sum > 0:
            end -= 1
        else:
            start += 1

print(result[0], result[1], result[2])