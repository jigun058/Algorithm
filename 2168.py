x, y = map(int,input().split())

def ceil(number):
    if number == int(number):
        return int(number)
    return int(number) + 1

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

mul = gcd(x, y)
x1 = x/mul
y1 = y/mul

print(int((x1 + y1 - 1)*mul))