# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)
#
# Answer: 872187

def is_palindrome(n):
	return str(n) == str(n)[::-1]

def is_palindrome_base2(n):
	return bin(n)[2:] == bin(n)[2:][::-1]

def main():
	total = 0
	for i in range(1, 1000000):
		if is_palindrome(i) and is_palindrome_base2(i):
			total += i
	print(total)

if __name__ == '__main__':
	main()