#	Largest palindrome product
#	Problem 4
#	A palindrome is a number that reads the same forwards and backwards.
#	For example, 5, 44, and 1111 are palindromes.
#	Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome_product(n):
    largest = 0
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            if is_palindrome(i * j):
                if i * j > largest:
                    largest = i * j
    return largest

def main():
    print(largest_palindrome_product(100))

if __name__ == "__main__":
    main()

