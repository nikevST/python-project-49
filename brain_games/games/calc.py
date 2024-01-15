import random
from brain_games.utils.generate_number import generate_number


DISCRIPTION = 'What is the result of the expression?'


def choose_operator():
    """
    Choose operator from the list of operators
    """
    operators = ['+', '-', '*']
    return random.choice(operators)


def generate_game():
    GAME_DIFFICULT = 10
    num1 = generate_number(GAME_DIFFICULT)
    num2 = generate_number(GAME_DIFFICULT)
    operator = choose_operator()
    result_dict = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
    }
    question = str(num1) + " " + operator + " " + str(num2)
    return (question, str(result_dict[operator]))
