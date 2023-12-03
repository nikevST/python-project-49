from brain_games.generate_number import generate_number
from brain_games.is_prime import is_number_prime


'''
function generate number and ask player "is it prime"
MIN_SIMPLE_NUMBER multiplies by generating number
'''


def prime_game(name: 'str'):
    GAME_ROUNDS = 3
    MIN_SIMPLE_NUMBER = 2
    GAME_DIFFICULT_LEVEL = 10
    for _ in range(GAME_ROUNDS):
        random_number = generate_number(GAME_DIFFICULT_LEVEL)\
                        + MIN_SIMPLE_NUMBER
        expected_answer = "yes" if is_number_prime(random_number) else "no"
        print("Answer \"yes\" if number is prime, otherwise answer \"no\" ")
        print(f"Question: {random_number}")
        answer = input("Your answer: ")
        if expected_answer == answer:
            print('Correct!')
        else:
            print(f"\"{answer}\" is a wrong answer ;(."
                 f"Correct answer is \"{expected_answer}\".")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")

