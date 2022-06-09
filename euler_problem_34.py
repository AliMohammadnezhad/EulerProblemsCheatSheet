# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers, less than one million, that are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#
# Answer: 40730
#

def main():
    sum = 0
    for i in range(3, 1000000):
        if i == sum_of_factorials(i):
            sum += i
    print(sum)

def sum_of_factorials(num):
    sum = 0
    for digit in str(num):
        sum += factorial(int(digit))
    return sum

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

if __name__ == '__main__':
    main()