T = int(input())

for _ in range(T):
    N = int(input())
    appli = []
    isFail = [0]*N
    for _ in range(N):
        appli.append(list(map(int, input().split())))
    
    appli.sort(key=lambda x: x[0])
    
    asdf = []
    asdf.append(appli[0][1])

    for i in range(N-1):
        if(appli[i][1]<appli[i+1][1]):
            appli[i+1][1] = appli[i][1]
        asdf.append(appli[i+1][1])
    
    print(len(set(asdf)))