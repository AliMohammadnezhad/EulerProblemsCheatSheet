# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
# Answer: 162

import itertools

fname = 'resources/problem_42/p042_words.txt'

def compute():
	ans = sum(1
		for s in open_file()
		if is_triangular_number(sum((ord(c) - ord('A') + 1) for c in s)))
	return str(ans)

def open_file():
    with open(fname) as f:
        return f.read().replace('"', '').split(',')

def is_triangular_number(n):
	temp = 0
	for i in itertools.count():
		temp += i
		if n == temp:
			return True
		elif n < temp:
			return False

if __name__ == "__main__":
	print(compute())