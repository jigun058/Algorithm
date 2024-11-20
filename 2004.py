def count_factors(num, factor):
    count = 0
    while num > 0:
        num //= factor
        count += num
    return count

n, m = map(int, input().split())

two_n = count_factors(n, 2)
two_m = count_factors(m, 2)
two_k = count_factors(n - m, 2)

five_n = count_factors(n, 5)
five_m = count_factors(m, 5)
five_k = count_factors(n - m, 5)

two = two_n - (two_m + two_k)
five = five_n - (five_m + five_k)

print(min(two, five))