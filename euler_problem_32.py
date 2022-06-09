# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# Hint: Some products can be obtained in more than one way so be sure to only include it once in your sum.
#
# Answer: 45228

def main():
    p = set()                                                    
    for a in range(1, 100):
        for b in range(1, 9999 // a):
            if ''.join(sorted("%d%d%d" % (a, b, a*b))) == '123456789':
                p.add(a * b)
    print(sum(p))

if __name__ == '__main__':
    main()