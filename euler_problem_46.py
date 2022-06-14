# Goldbach's other conjecture
# Problem 46
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
# Answer: 5777

import itertools

def compute():
	ans = next(itertools.filterfalse(test_goldbach, itertools.count(9, 2)))
	return str(ans)


def test_goldbach(n):
	if n % 2 == 0 or is_prime(n):
		return True
	for i in itertools.count(1):
		k = n - 2 * i * i
		if k <= 0:
			return False
		elif is_prime(k):
			return True

def sqrt(x):
	assert x >= 0
	i = 1
	while i * i <= x:
		i *= 2
	y = 0
	while i > 0:
		if (y + i)**2 <= x:
			y += i
		i //= 2
	return y

# Tests whether the given integer is a prime number.
def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, sqrt(x) + 1, 2):
			if x % i == 0:
				return False
		return True

if __name__ == "__main__":
	print(compute())