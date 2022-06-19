# Prime digit replacements - Problem 51
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
# Consequently 56003, being the first member of this family, is the smallest prime with this property.
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
# Answer: 121313
#

def solve(lim, places):
    primes = [num for num in range(2, 1000000) if all(num % i for i in range(2, int(round(num**0.5 + 1)))) 
                                                    and len(str(num)) - len(set(str(num))) >= places]
    for prime in primes:
        duplicates = {}
        generate_nums = []
        generate_primes = []
        for num in str(prime):
            if num in duplicates:
                duplicates[num] += 1
            else:
                duplicates[num] = 1
        for duplicate in [k for k, v in duplicates.items() if v > 1]:
            replacers = [str(i) for i in range(10)]
            generate_nums.append([int(str(prime).replace(duplicate, replacer)) for replacer in replacers])
        for generate_row in generate_nums:
            primes_count = 0
            for generate_num in generate_row:
                if generate_num in primes and len(str(generate_num)) == len(str(prime)):
                    primes_count += 1
            generate_primes.append(primes_count)
        if len(generate_primes) > 0 and max(generate_primes) == lim:
            return prime

def main():
    print(solve(8, 3))

if __name__ == '__main__':
    main()