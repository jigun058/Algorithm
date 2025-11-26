N = input()

#sumOfDigits = 0
#countZero = 0
digits = [int(digit) for digit in str(N)]

digits.sort(reverse=True)

num = 0
p = len(digits)-1
for i in digits:
    num += i*(10**p)
    p -= 1

if(num % 30 == 0):
    print(num)
else:
    print("-1")

