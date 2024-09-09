# N 이하의 소수를 구하는 함수 
def sieve_of_eratosthenes(N):
    # N 크기의 리스트를 만들어서 모든 수를 소수(True)라고 가정
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False  # 0과 1은 소수가 아니니까 지운다

    # !!중요!! 2부터 "루트N까지" 소수의 배수를 지움 -  간단한 최적화이니 해줍시다
    for prime in range(2, int(N ** 0.5) + 1):
        if sieve[prime]:  # prime이 소수인 경우
            for multiple in range(prime * prime, N + 1, prime):
                sieve[multiple] = False  # 'prime의 배수는 소수가 아닙니다' 라고 설정

    # 소수 반환하기
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes

