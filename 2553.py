def factorial(n):
    result = 1
    two_count = 0
    five_count = 0
    
    for i in range(2, n + 1):
        num = i
        
        while num % 2 == 0:
            num //= 2
            two_count += 1
        
        while num % 5 == 0:
            num //= 5
            five_count += 1
        
        result *= num
        result %= 10
    
    extra_twos = two_count - five_count
    result *= (2 ** extra_twos) % 10
    result %= 10
    return result

N = int(input())
print(factorial(N))