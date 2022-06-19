def solve():
    """ Compute the answer to Project Euler's problem #47 """

    target = 4  # number of prime factors and successive integers
    limit = 150000  # arbitrary upper-bound on the search, found by trial and error
    n_prime_divisors = [0] * limit  # the number of prime divisors of each integer considered

    run_length = 0  # length of the current run of valid integers
    for n in range(2, limit):
        if n_prime_divisors[n] == 0:
            # n is prime, sieve out multiples of n
            for m in range(2 * n, limit, n):
                n_prime_divisors[m] += 1  # m is divisible by n (prime)
            run_length = 0  # n is invalid, reset our run counter
        elif n_prime_divisors[n] == target:
            run_length += 1  # n is valid, increment our run counter
        else:
            run_length = 0  # n is invalid, reset our run counter

        if run_length == target:
            return n - target + 1  # we've found the smallest target run


if __name__ == '__main__':
	print(solve())