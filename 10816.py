N = int(input())
card = list(map(int, input().split()))
M = int(input())
toFind = list(map(int, input().split()))

card.sort()

nums = []

if N == 1:
    for i in toFind:
        if i == card[0]:
            nums.append(1)
        else:
            nums.append(0)
            continue

else:
    for i in toFind:
        count = 0

        first = 0
        last = len(card)-1
        mid = (len(card)-1)//2

        if card[0] == i:
            j = first
            while i == card[j]:
                count += 1
                j += 1
            nums.append(count)
            continue

        if card[-1] == i:
            j = last
            while i == card[j]:
                count += 1
                j -= 1
            nums.append(count)
            continue


        while(first+1 != last):
            if(i < card[mid]):
                last = mid
                mid = (first + last)//2
            elif(i > card[mid]):
                first = mid
                mid = (first + last)//2
            else:
                j = mid
                while i == card[j]:
                    count += 1
                    j += 1
                
                j = mid-1
                while i == card[j]:
                    count += 1
                    j -= 1

                break
        
        nums.append(count)

for i in nums:
    print(i, end=" ")
print()