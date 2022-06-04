#euler problem 2

first_number = 1
second_number = 2
sum_of_even_numbers = 0

def check_even(n):
    if n%2 == 0:
        return True
    else:
        return False


while first_number < 4000000:
    if check_even(first_number):
        sum_of_even_numbers += first_number
    first_number, second_number = second_number, first_number + second_number


print(sum_of_even_numbers)