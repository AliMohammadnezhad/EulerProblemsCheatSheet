# Euler discovered the remarkable quadratic formula:
# n² + n + 41
# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.
# The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.
# Considering quadratics of the form:
# n² + an + b, where |a| < 1000 and |b| < 1000
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |−4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
# Answer: -59231

import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def get_primes(n):
    primes = []
    for i in range(n+1):
        if is_prime(i):
            primes.append(i)
    return primes

def get_coefficients(n):
    primes = get_primes(n)
    for a in range(-999, 1000):
        for b in primes:
            if is_prime(abs(a) + b):
                return a, b

def get_n(a, b):
    n = 0
    while is_prime(n**2 + a*n + b):
        n += 1
    return n

def get_max_n(n):
    max_n = 0
    max_a = 0
    max_b = 0
    for a in range(-999, 1000):
        for b in get_primes(n):
            n = get_n(a, b)
            if n > max_n:
                max_n = n
                max_a = a
                max_b = b
    return max_a, max_b

def main():
    max_a, max_b = get_max_n(1000)
    print(max_a * max_b)

if __name__ == '__main__':
    main()