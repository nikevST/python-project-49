'''
    Function hide random progression element
    Player trying to guess it
'''


import random
from brain_games.generate_progression import generate_arithmetic_progression
from brain_games.question_answer import q_a_func


def progression_game(name):
    GAME_ROUNDS = 3
    print("What number is missing in the progression?")
    for _ in range(GAME_ROUNDS):
        arithmetic_progression_list = generate_arithmetic_progression()
        hiding_progression_elem = random.choice(arithmetic_progression_list)
        sequence_string = ""
        for elem in arithmetic_progression_list:
            if elem == hiding_progression_elem:
                sequence_string += ".."
            else:
                sequence_string += f"{str(elem)}"
        result = q_a_func(' '.join(sequence_string), str(hiding_progression_elem))
        if not result:
            print(f"Let\'s try again, {name}!")
            return
    print(f"Congratulations, {name}!")
