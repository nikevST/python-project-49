import random
from brain_games.generate_number import generate_number


def choose_operator():
    """
    Choose operator from the list of operators
    """
    operators = ['+', '-', '*']
    return random.choice(operators)


def choose_difficult():
    """
    User enter game difficult rate
    To use function, insert it into "difficult_rate" result
    """
    num = input('Choose difficult from 1 to 10, or press Enter: ')
    if num.isdigit():
        if int(num) > 0 and int(num) < 11:
            if int(num) > 3:
                print('Nice choice! Please, dont use calc!')
            return int(num)
        else:
            return 1
    else:
        return 1


def brain_calc(name):
    GAME_ROUNDS = 3
    GAME_DIFFICULT = 10
    difficult_rate = GAME_DIFFICULT
    for _ in range(GAME_ROUNDS):
        num1 = generate_number(difficult_rate)
        num2 = generate_number(difficult_rate)
        operator = choose_operator()
        result_dict = {
          '+': num1 + num2,
          '-': num1 - num2,
          '*': num1 * num2,
        }
        print('What is the result of the expression?: ')
        print(f'{num1} {operator} {num2}')
        answer = input('Your answer is: ')
        if str(result_dict[operator]) == answer:
            print('Correct!')
        else:
            print(f'{answer} is a wrong answer.' 
            f'The correct answer is {result_dict[operator]}')
            print(f'Try again, {name}')
            return
    print(f'Congratulations, {name}')

