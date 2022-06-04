# 	Summation of primes - Problem 10
# 	Problem 10
# 	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 	Find the sum of all the primes below two million.
#
def main():
     sum = 0
     for i in range(2, 2000000):
         if is_prime(i):
             sum += i
     print(sum)

def is_prime(n):
     if n == 1:
         return False
     for i in range(2, int(n**0.5) + 1):
         if n % i == 0:
             return False
     return True

if __name__ == '__main__':
     main()