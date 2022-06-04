# 10001st prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def main():
    n = 1
    count = 0
    while count < 10001:
        n += 1
        if is_prime(n):
            count += 1
    print(n)

if __name__ == '__main__':
    main()

