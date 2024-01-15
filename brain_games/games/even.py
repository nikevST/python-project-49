'''
    function print number and asked is it even or not
    player should answer 'yes' or 'no'
'''


from brain_games.utils.generate_number import generate_number


DISCRIPTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def is_even(number: 'int'):
    return False if number % 2 else True


def generate_game():
    MIN_NUMBER = 1
    GAME_DIFFICULT = 10
    random_number = generate_number(GAME_DIFFICULT) + MIN_NUMBER
    expected_answer = "yes" if is_even(random_number) else "no"
    return (str(random_number), str(expected_answer))
