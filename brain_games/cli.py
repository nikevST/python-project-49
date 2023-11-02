import prompt


def welcome_user():
    name = prompt.string('Enter your name, please ')
    print(f'Hello, {name}!')


# if __name__ == '__main__':
#    welcome_user()
