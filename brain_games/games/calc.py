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
    difficult_rate = choose_difficult()
    for _ in range(0,3):
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

