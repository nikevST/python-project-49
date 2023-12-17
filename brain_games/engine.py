import prompt


def q_a_func(some_value: 'str', expected_answer: 'str'):
    print(f"Question: {some_value}")
    answer = input("Your answer: ")
    if expected_answer == answer:
        print('Correct!')
        return True
    else:
        print(f"\'{answer}\' is a wrong answer ;(. "
              f"Correct answer was \'{expected_answer}\'.")
        return False


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'{game.__doc__}') 
    ROUNDS = 3
    for _ in range(0, ROUNDS):
        answer, correct_answer = game(name)
        result = q_a_func(answer, correct_answer)    
        if not result:
            print(f"Let\'s try again, {name}!")
            return
    print(f"Congratulations, {name}!")    
