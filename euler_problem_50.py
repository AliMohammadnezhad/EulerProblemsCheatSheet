# Consecutive prime sum - Problem 50
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
# Answer: 997651
#
def solve():
    primes = [2]
    for i in range(3, 1000000, 2):
        if is_prime(i):
            primes.append(i)
    max_len = 0
    max_prime = 0
    for i in range(len(primes)):
        sum = 0
        for j in range(i, len(primes)):
            sum += primes[j]
            if sum > 1000000:
                break
            if is_prime(sum):
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    max_prime = sum
    return max_prime

def is_prime(n):
    return all(n % i for i in range(2, int(round(n**0.5 + 1))))

def main():
    print(solve())

if __name__ == '__main__':
    main()