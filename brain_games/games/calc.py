import random
from brain_games.utils.generate_number import generate_number
#from brain_games.question_answer import q_a_func


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
    '''What is the result of the expression?'''
   # GAME_ROUNDS = 3
    GAME_DIFFICULT = 10
   # print('What is the result of the expression?')
   # for _ in range(GAME_ROUNDS):
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
      #  if not result:
     #       print(f"Let\'s try again, {name}!")
    #        return
   # print(f"Congratulations, {name}!")
