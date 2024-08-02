count = 1
title = 665
pow = 2
isEnd=0
N = int(input())

while(N >= count):
    title += 1
    for i in range(len(str(title))-2):
        if(str(title)[i] == "6"):
            if(str(title)[i+1] == "6"):
                if(str(title)[i+2] == "6"):
                    isEnd = 1
                    break
    if(isEnd==1):
        count += 1
        isEnd = 0

print(title)