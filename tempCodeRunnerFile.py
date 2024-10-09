N = int(input())
vals = list(map(int,input().split()))

vals.sort()
result = []

for i in range(len(vals)-2):

    start = i+1
    end = len(vals)-1
    min = 3000000001

    while start < end:
        if vals[i] + vals[start] + vals[end] > 0:
            end -= 1
            if abs(vals[i] + vals[start] + vals[end]) < min:
                min = abs(vals[i] + vals[start] + vals[end])
                mem = [i, start, end]

        else:
            start += 1
            if abs(vals[i] + vals[start] + vals[end]) < min:
                min = abs(vals[i] + vals[start] + vals[end])
                mem = [i, start, end]

    result.append([vals[mem[0]], vals[mem[1]], vals[mem[2]], min])

result.sort(key=lambda x:x[3])
for i in range(3):
    print(result[0][i], end=" ")
print()