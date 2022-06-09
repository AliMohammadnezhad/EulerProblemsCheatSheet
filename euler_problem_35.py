# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?
#
# Answer: 55
#

import itertools
import math



def prime(n): #function to find prime no in the given Range
	for x in range(2, int(math.sqrt(n)) + 1):
		if (n%x)==0:
			break
	else:
		return n 
			
def cirpirme(n): #Function to classify if the prime no is circular prime or not
	no=str(n)
	for x in range(0,len(no)):
			r = no[x:len(no)] + no[0:x]
			if not prime(int(r)) :
				return False
	return True

def main():
    count=0
    for x in range(2,1000000):
        if cirpirme(x):
            count+=1
    print(count)


if __name__ == '__main__':
    main()