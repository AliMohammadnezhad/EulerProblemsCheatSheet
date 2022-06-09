# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?
#
# Answer: 840
#


def compute():
	ans = max(range(1, 1001), key=count_solutions)
	return str(ans)


def count_solutions(p):
	result = 0
	for a in range(1, p + 1):
		for b in range(a, (p - a) // 2 + 1):
			c = p - a - b  # c >= b
			if a * a + b * b == c * c:
				result += 1
	return result


if __name__ == "__main__":
	print(compute())