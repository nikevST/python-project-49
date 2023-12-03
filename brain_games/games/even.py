from brain_games.generate_number import generate_number 


#def make_random_number(sequence : 'str'):
#    return int(ord(random.choice(sequence)))


def is_odd(number: 'int'):
    return 'no' if number % 2 else 'yes'


def brain_even_game(name: 'str'):
   # sequence = 'brain_even'
    GAME_ROUNDS = 3
    counter = 0
    while (counter < GAME_ROUNDS) :
        random_number = generate_number()
        expected_answer = is_odd(random_number)
        print("Answer \"yes\" if number is even, otherwise answer \"no\" ")
        print(f"Question: {random_number}")
        answer = input("Your answer: ")
        if expected_answer == answer:
            print('Correct!')
            counter += 1
        else:
            print(f"\"{answer}\" is a wrong answer ;(. Correct answer is \"{expected_answer}\".")
            print("Let's try again")
            return 
    print(f"Congratulation, {name}!")

