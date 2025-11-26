"""
toDelete = []


i = 0
while(i <= 10000) :
    sum = i
    sum += i%10
    sum += i//10%10
    sum += i//100%10
    sum += i//1000%10
    sum += i//10000%10

    toDelete.append(sum)
    i += 1


for i in range(1,10001):
    if():
        print(allNums[i])

        
"""

a = int(input())
b = int(input())
c = int(input())

sa = str(a)
sb = str(b)
sab = sa+sb
ab = int(sab)

print(a+b-c)
print(ab-c)