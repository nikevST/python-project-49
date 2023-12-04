def q_a_func(some_value: 'str', expected_answer: 'str'):
    print(f"Question: {some_value}")
    answer = input("Your answer: ")
    if expected_answer == answer:
        print('Correct!')
        return True
    else:
        print(f"\'{answer}\' is a wrong answer ;(. "
              f"Correct answer was \'{expected_answer}\'.")
        return False
