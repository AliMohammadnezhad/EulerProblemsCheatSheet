# Prime permutations - Problem 49
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?
# Answer: 296962999629


def solve():
  
    sequences = []                   
    for num in range(1235, 10000 - 3330 * 2, 2):
        num_1, num_2, num_3 = num, num + 3330, num + 3330 * 2
        if set(str(num_1)) == set(str(num_2)) == set(str(num_3)) and is_prime(num_1) and is_prime(num_2) and is_prime(num_3):
            sequences.append(str(num_1) + str(num_2) + str(num_3))
    return int(sequences[-1])

def is_prime(n):
    return all(n % i for i in range(2, int(round(n**0.5 + 1))))

if __name__ == '__main__':
    print(solve())