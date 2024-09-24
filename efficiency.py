
def mod_exp(a, b, m):
    result = 1
    a = a % m  # a를 m으로 나눈 나머지로 초기화
    
    while b > 0:
        if b % 2 == 1:  # b가 홀수인 경우
            result = (result * a) % m
        b = b // 2
        a = (a * a) % m
    
    return result
