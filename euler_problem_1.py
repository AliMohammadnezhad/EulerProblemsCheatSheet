# Iterative Solutions
numbers = [num for num in range(1, 1000)]


def check_multiples(*number: int):
    sum_of_multiples_number = 0
    for num in number:
        if num % 3 == 0 or num % 5 == 0:
            sum_of_multiples_number += num

    return sum_of_multiples_number


print(check_multiples(*numbers))

# Using List Comprehensions

print(sum(num for num in range(1, 1000) if num % 3 == 0 or num % 5 == 0))

# Using filter()

print(sum(filter(lambda num: num % 3 == 0 or num % 5 == 0, range(1, 1000))))
