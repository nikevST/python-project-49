import prompt

'''
run_game() recieve game function as argument, print greet message,
make player name request
'''

def run_game(game: "function"):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    game(name)

