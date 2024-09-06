N, M = map(int, input().split())

pan = list(input() for _ in range(N))

fromWhite = []
fromBlack = []

inRow = M-7
inCol = N-7

def makeWhite(line):
    count = 0
    for i in range(0, 8, 2):
        if line[i] == "B":
            count += 1
    for i in range(1, 9, 2):
        if line[i] == "W":
            count += 1
    return count

def makeBlack(line):
    count = 0
    for i in range(0, 8, 2):
        if line[i] == "W":
            count += 1
    for i in range(1, 9, 2):
        if line[i] == "B":
            count += 1
    return count
    

for i in range(N):
    wtemp = []
    btemp = []
    
    for j in range(inRow):
        line = pan[i][j:j+8]
        wtemp.append(makeWhite(line))
        btemp.append(makeBlack(line))
    
    fromWhite.append(wtemp)
    fromBlack.append(btemp)
    
    
for a in range(1, N, 2):
    temp = fromWhite[a]
    fromWhite[a] = fromBlack[a]
    fromBlack[a] = temp
    
min = 2500

for i in range(inCol):
    for j in range(inRow):
        sum = 0
        for k in range(8):
            sum += fromBlack[i+k][j]    
        if sum < min:
            min = sum
        
        sum = 0
        for k in range(8):
            sum += fromWhite[i+k][j]    
        if sum < min:
            min = sum
                
print(min)