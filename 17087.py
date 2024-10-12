N, S = map(int, input().split())
A = list(map(int, input().split()))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

for i in range(len(A)):
    if A[i] >= S:
        A[i] = A[i] - S
    else:
        A[i] = S - A[i]

for i in range(len(A)-1):
    A[i+1] = gcd(A[i], A[i+1])

print(A[-1])