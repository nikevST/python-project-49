import random


def make_random_number(sequence : 'str'):
    return int(ord(random.choice(sequence)))


def is_odd(number : 'int'):
  return 'no' if number % 2 else 'yes'


def brain_even_game(name: 'str'):
  sequence = 'brain_even'
  counter = 0
  while (counter < 3) :
    random_number = make_random_number(sequence)
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
  print(f"congratulation, {name}!")

