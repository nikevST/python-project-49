import random
from brain_games.generate_number import generate_number


def choose_operator():
    """
    Choose operator from the list of operators
    """
    operators = ['+', '-', '*']
    return random.choice(operators)


def brain_calc(name):
    for _ in range(0,3):
        num1 = generate_number()
        num2 = generate_number()
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

