N = int(input())
size = list(map(int, input().split()))

size.sort()

if N == 1:
    print("0")

elif N == 2:
    if size[0]*10//9 >= size[1]:
        print("1")
    else:
        print("0")
    
else:
    count = 0
    for i in range(len(size)-1):
        bound = size[i]*10//9
        
        if size[-1] <= bound:
            count += len(size)-i-1
            continue
        if bound < size[i+1]:
            continue
        
        first = i+1
        last = len(size)-1
        mid = (first + last)//2

        while(first+1 != last):
            if(bound < size[mid]):
                last = mid
                mid = (first + last)//2
            elif(bound >= size[mid]):
                first = mid
                mid = (first + last)//2
        
        count += first - i
        
    print(count)