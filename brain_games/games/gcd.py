'''
function shows two random numbers
player should type grand common divisor of numbers
'''


from brain_games.generate_number import generate_number
from brain_games.find_gcd import find_gcd
from brain_games.question_answer import q_a_func


def gcd_game(name):
    print("Find the greatest common divisor of given numbers.")
    GAME_ROUNDS = 3
    GAME_DIFFICULT = 10
    for _ in range(GAME_ROUNDS):
        num1 = generate_number(GAME_DIFFICULT)
        num2 = generate_number(GAME_DIFFICULT)
        while not num1 or not num2:
            num1 = generate_number(GAME_DIFFICULT)
            num2 = generate_number(GAME_DIFFICULT)
        gcd_of_numbers = find_gcd(num1, num2)
        question = str(num1) + " " + str(num2)
        result = q_a_func(question, str(gcd_of_numbers))
        if not result:
            print(f"Let\'s try again, {name}!")
            return
    print(f"Congratulations, {name}!")
