a,b = map(int, input().split())
coDiv = 0
coMul = 0

if a>b :
    a,b = b,a   #a<b가 되도록

for i in range(a, 0, -1) :
    if a%i == 0 :
        if b%i == 0 :
            coDiv = i
            break

coMul = int(a*b/i)

print(coDiv)
print(coMul)