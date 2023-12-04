import prompt


'''
    run_game() recieve game function as argumen,
    print greet message, request player name
'''


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    game(name)
