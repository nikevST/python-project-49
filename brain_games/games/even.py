'''
    function print number and asked is it even or not
    player should answer 'yes' or 'no'
'''


from brain_games.utils.generate_number import generate_number


DISCRIPTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def is_odd(number: 'int'):
    return 'no' if number % 2 else 'yes'


def generate_game():
    MIN_NUMBER = 1
    GAME_DIFFICULT = 10
    random_number = generate_number(GAME_DIFFICULT) + MIN_NUMBER
    expected_answer = is_odd(random_number)
    return (str(random_number), str(expected_answer))
