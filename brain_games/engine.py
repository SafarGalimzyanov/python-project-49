from prompt import string
from random import randrange, choice


GAME_DURATION = 3  # the game ends after 3 correct answers in a row


def get_random_num(min_num: int, max_num: int) -> int:
    return randrange(min_num, max_num + 1)


def get_random_elem(t: tuple):
    return choice(t)


def play_game(game_rule: str, questions: list, right_answers: list) -> None:
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!\n{game_rule}')

    for i in range(GAME_DURATION):
        print(f'Question: {questions[i]}')
        user_answer = string('Your answer: ')

        if user_answer == right_answers[i]:  # continue
            print('Correct!')
        else:  # exit
            print(f'"{user_answer}" is a wrong answer ;(. Correct answer was "{right_answers[i]}".')
            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
