#n의 약수를 구하는 함수
def find_divisors_by_definition(n):
    divisors = []
    
    # 1부터 n까지 모든 숫자에 대해 나누어 떨어지는지 확인하기
    for i in range(1, n + 1):
        if n % i == 0:  # n을 i로 나눴을 때 나머지 0이면 i는 n의 약수
            divisors.append(i)
    
    #약수 반환하기
    return divisors

