# Convert an integer to binary
def convert(n):
    # Base Case
    if n == 1:
        return "1"
    # Recursive call
    binary = n % 2
    return convert(n//2) + str(binary)


print(convert(37))


def sum_of_first_n_odd_integers(n):
    # Base Case
    if n == 1:
        return 1
    odd_number = 2*n - 1
    # recursive call
    return odd_number + sum_of_first_n_odd_integers(n-1)


# print(sum_of_first_n_odd_integers(5))


def sum_of_first_n_even_integers(n):
    # Base Case
    if n == 0:
        return 0
    even_number = 2*n
    # Recursive call
    return even_number + sum_of_first_n_even_integers(n-1)


# print(sum_of_first_n_even_integers(4))


def sum_of_odd_numbers(n):
    # Base case
    if n == 1:
        return 1
    # Condition to check for even numbers
    if n % 2 != 0:
        # recursive call
        return n + sum_of_odd_numbers(n-1)
    else:
        return sum_of_odd_numbers(n-1)


# print(sum_of_odd_numbers(5))
