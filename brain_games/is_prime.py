from math import sqrt


def is_number_prime(number):
    return all(number % divider for divider in range(2, int(sqrt(number) + 1)))

