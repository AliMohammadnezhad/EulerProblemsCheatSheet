# Lattice paths - Problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
#
# Answer: 137846528820

def lattice_paths(n):
    return factorial(2*n) // (factorial(n)**2)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def main():
    print(lattice_paths(20))

if __name__ == "__main__":
    main()