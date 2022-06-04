# Sum squrares of the first 100 natural numbers

def sum_squares(n):
    return sum(i**2 for i in range(1, n+1))

def square_sum(n):
    return sum(range(1, n+1))**2

def main():
    print(square_sum(100) - sum_squares(100))

if __name__ == '__main__':
    main()