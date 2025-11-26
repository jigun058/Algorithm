N = int(input())
NN = int(input())

table = [[0]*N for _ in range(N)]
count = 2
floor = 2

mx = 0
my = 0

def check():
    global mx
    global my
    if count == NN:
        mx = row+1
        my = col+1

row = N//2
col = N//2
table[row][col] = 1
if NN == 1:
    mx = row+1
    my = col+1

while floor <= N//2+1:
    right, down, left, up = floor*2-3, floor*2-2, floor*2-2, floor*2-2
    
    row = N//2-floor+1
    col = N//2-floor+2
    
    table[row][col] = count
    check()
    count += 1
    
    for _ in range(right):
        col += 1
        table[row][col] = count
        check()
        count += 1
    
    for _ in range(down):
        row += 1
        table[row][col] = count
        check()
        count += 1
        
    for _ in range(left):
        col -= 1
        table[row][col] = count
        check()
        count += 1
        
    for _ in range(up):
        row -= 1
        table[row][col] = count
        check()
        count += 1
    
    floor += 1

for i in range(N):
    for j in range(N):
        print(table[i][j], end = " ")
    print()

print(mx, my)