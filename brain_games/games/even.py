'''
    function print number and asked is it even or not
    player should answer 'yes' or 'no'
'''

from brain_games.generate_number import generate_number
from brain_games.question_answer import q_a_func


def is_odd(number: 'int'):
    return 'no' if number % 2 else 'yes'


def brain_even_game(name: 'str'):
    GAME_ROUNDS = 3
    GAME_DIFFICULT = 10
    MIN_NUMBER = 1
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    for _ in range(GAME_ROUNDS):
        random_number = generate_number(GAME_DIFFICULT) + MIN_NUMBER
        expected_answer = is_odd(random_number)
        result = q_a_func(str(random_number), str(expected_answer))
        if not result:
            print(f"Let\'s try again, {name}!")
            return
    print(f"Congratulations, {name}!")
