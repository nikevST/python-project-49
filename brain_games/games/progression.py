'''
    Function hide random progression element
    Player trying to guess it
'''


import random
from brain_games.question_answer import q_a_func
from brain_games.utils.generate_number import generate_number


def generate_arithmetic_progression():
    '''
    Function generate arithmetic progression using random()
    MAX progression length = 15
    '''
    MIN_PROGRESSION_LENGTH = 5
    MIN_PROGRESSION_STEP = 1
    progression_length = generate_number() + MIN_PROGRESSION_LENGTH
    first_progression_elem = generate_number()
    progression_step = generate_number() + MIN_PROGRESSION_STEP
    current_elem = first_progression_elem
    progression_list = []
    for _ in range(progression_length):
        progression_list.append(current_elem)
        current_elem += progression_step
    return progression_list


def progression_game(name):
    GAME_ROUNDS = 3
    print("What number is missing in the progression?")
    for _ in range(GAME_ROUNDS):
        arithmetic_progression_list = generate_arithmetic_progression()
        hiding_progression_elem = random.choice(arithmetic_progression_list)
        sequence_string = ""
        for elem in arithmetic_progression_list:
            if elem == hiding_progression_elem:
                sequence_string += ".. "
            else:
                sequence_string += f"{str(elem)} "
        result = q_a_func(sequence_string.strip(), str(hiding_progression_elem))
        if not result:
            print(f"Let\'s try again, {name}!")
            return
    print(f"Congratulations, {name}!")
