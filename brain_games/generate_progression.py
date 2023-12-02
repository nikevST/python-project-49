from brain_games.generate_number import generate_number


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

