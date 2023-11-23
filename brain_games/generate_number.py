import random


def generate_number():
    """
    Generate random number using seed()
    """
    random.seed()
    return int(random.random() * 10)
