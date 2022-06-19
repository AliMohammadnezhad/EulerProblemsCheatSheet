# Self powers - Problem 48
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
# Answer: 9110846700

def solve():
    """ Compute the answer to Project Euler's problem #48 """

    limit = 1000
    sum = 0
    for i in range(1, limit + 1):
        sum += i ** i
    return str(sum)[-10:]

if __name__ == '__main__':
    print(solve())