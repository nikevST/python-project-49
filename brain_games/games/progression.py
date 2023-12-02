import random
from brain_games.generate_progression import generate_arithmetic_progression


def progression_game(name):
    '''
    Function recieve another function which generetes progression
    Current function "hiding" one random choisen progression element
    Player trying to guess it
    '''
    GAME_ROUNDS = 3
    for _ in range(GAME_ROUNDS):
        arithmetic_progression_list = generate_arithmetic_progression()
        hiding_progression_elem = random.choice(arithmetic_progression_list)
        sequence_string = ""
        for elem in arithmetic_progression_list:
            if elem == hiding_progression_elem:
                sequence_string += " .. "
            else:
                sequence_string += f" {str(elem)} "
        print("What number is missing in the progression?")
        print(f"Question: {sequence_string}")
        answer = input("Your answer is ")
        if answer == str(hiding_progression_elem):
            print("Correct!")
        else:
            print(f'\'{answer}\' is a wrong answer ;(.' 
            f'The correct answer was \'{hiding_progression_elem}\'')
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')

