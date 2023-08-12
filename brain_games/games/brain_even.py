#!/usr/bin/env python3


# description
GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no"'
MIN_NUM = 1
MAX_NUM = 99


def get_question_answer(get_random_num) -> tuple:
    random_num = get_random_num(MIN_NUM, MAX_NUM)
    question = random_num
    answer = 'yes' if random_num % 2 == 0 else 'no'

    return (question, answer)


def init_game(get_random_num, GAME_DURATION: int) -> tuple:
    questions, answers = [None]*GAME_DURATION, [None]*GAME_DURATION
    for i in range(GAME_DURATION):
        questions[i], answers[i] = get_question_answer(get_random_num)

    return (GAME_RULE, questions, answers)
