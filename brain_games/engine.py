import prompt

'''
run_game() recieve game function as argument, print greet message,
make player name request
'''

def run_game(game: "function"):
    print('Welcome to Brain Games!')
    name = prompt.string('Enter your name, please: ')
    print(f'Hello, {name}!')
    game(name)

