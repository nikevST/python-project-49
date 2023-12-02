from brain_games.generate_number import generate_number
from brain_games.find_gcd import find_gcd


def gcd_game(name):
    print("Find the greatest common divisor for given numbers.")
    max_game_rounds = 3
    num1 = 0
    num2 = 0
    while max_game_rounds > 0:
        num1 = generate_number(10)
        num2 = generate_number(10)
        while not num1 or not num2:
            num1 = generate_number(10)
            num2 = generate_number(10)
        gcd_of_numbers = find_gcd(num1, num2)
        print(f"Question: {num1} {num2}")
        answer = input('Your answer is: ')
        if str(gcd_of_numbers) == answer:
            print('Correct!')
            max_game_rounds -= 1
        else:
            print(f'{answer} is a wrong answer.'
            f'The correct answer is {gcd_of_numbers}')
            print(f'Try again, {name}')
            return
    print(f'Congratulations, {name}')

