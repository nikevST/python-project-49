from brain_games.generate_number import generate_number
from brain_games.find_gcd import find_gcd


def gcd_game(name):
    print("Find the greatest common divisor for given numbers.")
    GAME_ROUNDS = 3
    GAME_DIFFICULT = 10
    for _ in range(GAME_ROUNDS):
        num1 = generate_number(GAME_DIFFICULT)
        num2 = generate_number(GAME_DIFFICULT)
        while not num1 or not num2:
            num1 = generate_number(GAME_DIFFICULT)
            num2 = generate_number(GAME_DIFFICULT)
        gcd_of_numbers = find_gcd(num1, num2)
        print(f"Question: {num1} {num2}")
        answer = input('Your answer is: ')
        if str(gcd_of_numbers) == answer:
            print('Correct!')
        else:
            print(f'{answer} is a wrong answer.'
            f'The correct answer is {gcd_of_numbers}')
            print(f'Try again, {name}')
            return
    print(f'Congratulations, {name}')

