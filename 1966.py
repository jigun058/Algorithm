case = int(input())

for i in range(case):

    n, m = map(int, input().split())
    docs = list(map(int, input().split()))

    count = 0
    index = 0

    docsSorted = (docs.sort()).reverse()
    
    