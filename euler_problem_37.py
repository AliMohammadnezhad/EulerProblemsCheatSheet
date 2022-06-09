# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
#
# Answer: 748317
#
import math
def is_prime(n):
    if n == 1:
        return False
    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True
def is_truncatable_prime(n):
    if not is_prime(n):
        return False
    n = str(n)
    for i in range(1, len(n)):
        if not is_prime(int(n[i:])):
            return False
        if not is_prime(int(n[:-i])):
            return False
    return True
def main():
    count = 0
    for x in range(11, 1000000):
        if is_truncatable_prime(x):
            count += x
    print(count)
if __name__ == '__main__':
    main()
