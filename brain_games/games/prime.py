'''
function generate number and ask player "is it prime"
MIN_SIMPLE_NUMBER multiplies by generating number
'''

from brain_games.generate_number import generate_number
from brain_games.is_prime import is_number_prime
from brain_games.question_answer import q_a_func


def prime_game(name: 'str'):
    GAME_ROUNDS = 3
    MIN_SIMPLE_NUMBER = 2
    GAME_DIFFICULT_LEVEL = 10
    print("Answer \"yes\" if given number is prime. "
          "Otherwise answer \"no\".")
    for _ in range(GAME_ROUNDS):
        random_number = generate_number(GAME_DIFFICULT_LEVEL)\
            + MIN_SIMPLE_NUMBER
        expected_answer = "yes" if is_number_prime(random_number) else "no"
        result = q_a_func(str(random_number), expected_answer)
        if not result:
            print(f"Let\'s try again, {name}!")
            return
    print(f"Congratulations, {name}!")
