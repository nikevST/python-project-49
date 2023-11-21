import prompt
from brain_games.games.even import brain_even_game 


def hello_user():
    name = prompt.string('Enter your name, please ')
    print(f'Hello, {name}!')
    return name


def even_game():
    name = hello_user()
    brain_even_game(name)

