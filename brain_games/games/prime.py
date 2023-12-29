'''
function generate number and ask player "is it prime"
MIN_SIMPLE_NUMBER multiplies by generating number
'''


from brain_games.utils.generate_number import generate_number
from math import sqrt


DISCRIPTION = "Answer \"yes\" if given number is prime. "\
              "Otherwise answer \"no\"."


def is_number_prime(number):
    return all(number % divider
               for divider in range(2, int(sqrt(number) + 1)))


def generate_game():
    MIN_SIMPLE_NUMBER = 2
    GAME_DIFFICULT_LEVEL = 10
    random_number = generate_number(GAME_DIFFICULT_LEVEL)\
        + MIN_SIMPLE_NUMBER
    expected_answer = "yes" if is_number_prime(random_number) else "no"
    return (str(random_number), expected_answer)
