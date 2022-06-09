# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?
#
# Answer: 7652413

import eulerlib


def compute():
	# Note: The only 1-digit pandigital number is 1, which is not prime. Thus we require n >= 2.
	for n in reversed(range(2, 10)):
		arr = list(reversed(range(1, n + 1)))
		while True:
			if arr[-1] not in NONPRIME_LAST_DIGITS:
				n = int("".join(str(x) for x in arr))
				if eulerlib.is_prime(n):
					return str(n)
			if not prev_permutation(arr):
				break
	raise AssertionError()

NONPRIME_LAST_DIGITS = {0, 2, 4, 5, 6, 8}


def prev_permutation(arr):
	i = len(arr) - 1
	while i > 0 and arr[i - 1] <= arr[i]:
		i -= 1
	if i <= 0:
		return False
	j = len(arr) - 1
	while arr[j] >= arr[i - 1]:
		j -= 1
	arr[i - 1], arr[j] = arr[j], arr[i - 1]
	arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
	return True


if __name__ == "__main__":
	print(compute())