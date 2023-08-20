from prompt import string
from random import randrange, choice


GAME_DURATION = 3  # the game ends after 3 correct answers in a row


def get_random_num(min_num: int, max_num: int) -> int:
    return randrange(min_num, max_num + 1)


def get_random_elem(arr, index=False):
    if index:
        i = randrange(len(arr))
        return (arr[i], i)
    else:
        return choice(arr)


def play_game(GAME_RULE, get_question_answer) -> None:
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!\n{GAME_RULE}')

    for _ in range(GAME_DURATION):
        question, right_answer = get_question_answer()
        print(f'Question: {question}')
        user_answer = string('Your answer: ')

        if user_answer == right_answer:  # continue
            print('Correct!')
        else:  # exit
            print(f'"{user_answer}" is a wrong answer ;(. Correct answer was "{right_answer}".')
            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
