# Sub-string divisibility
# Problem 43
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
# Answer: 16695334890

import itertools


def compute():
	ans = sum(int("".join(map(str, num)))
		for num in itertools.permutations(list(range(10)))
		if is_substring_divisible(num))
	return str(ans)


DIVISIBILITY_TESTS = [2, 3, 5, 7, 11, 13, 17]

def is_substring_divisible(num):
	return all((num[i + 1] * 100 + num[i + 2] * 10 + num[i + 3]) % p == 0
		for (i, p) in enumerate(DIVISIBILITY_TESTS))


if __name__ == "__main__":
	print(compute())