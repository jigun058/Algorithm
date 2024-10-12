a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

sum_upper = a1*b2 + a2*b1
sum_lower = a2*b2

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if sum_upper > sum_lower:
    a = sum_upper
    b = sum_lower
else:
    a = sum_lower
    b = sum_upper

div = gcd(a, b)

print(str(sum_upper//div) + " " + str(sum_lower//div))