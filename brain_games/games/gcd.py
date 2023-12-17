'''
Find the greatest common divisor of given numbers.
'''


from brain_games.utils.generate_number import generate_number
#from brain_games.question_answer import q_a_func


def find_gcd(num1, num2):
    if num1 == num2:
        return num1
    if not num1 % num2:
        return num2
    if not num2 % num1:
        return num1
    less_num = num2 if num1 > num2 else num1
    nod = 1
    for iter in range(2, int(less_num / 2) + 1):
        if not num1 % iter and not num2 % iter:
            nod = iter
    return nod


def gcd_game(name):
    '''Find the greatest common divisor of given numbers.'''
   # print("Find the greatest common divisor of given numbers.")
   # GAME_ROUNDS = 3
    GAME_DIFFICULT = 10
   # for _ in range(GAME_ROUNDS):
    num1 = generate_number(GAME_DIFFICULT)
    num2 = generate_number(GAME_DIFFICULT)
    while not num1 or not num2:
        num1 = generate_number(GAME_DIFFICULT)
        num2 = generate_number(GAME_DIFFICULT)
    gcd_of_numbers = find_gcd(num1, num2)
    question = str(num1) + " " + str(num2)
    return (question, str(gcd_of_numbers))
    #    if not result:
     #       print(f"Let\'s try again, {name}!")
      #      return
# print(f"Congratulations, {name}!")
