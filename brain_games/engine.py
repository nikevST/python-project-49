import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DISCRIPTION)
    ROUNDS = 3
    for _ in range(0, ROUNDS):
        question, correct_answer = game.generate_game()
        print(f"Question: {question}")
        answer = input("Your answer: ")
        if correct_answer == answer:
            print('Correct!')
        else:
            print(f"\'{answer}\' is a wrong answer ;(. "
                  f"Correct answer was \'{correct_answer}\'.")
            print(f"Let\'s try again, {name}!")
            return
    print(f"Congratulations, {name}!")
