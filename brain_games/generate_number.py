import random


def generate_number(difficult_rate=1):
    """
    Generate random number using seed()
    """
    MAX_VALUE = 10
    random.seed()
    return int(random.random() * MAX_VALUE * difficult_rate)
