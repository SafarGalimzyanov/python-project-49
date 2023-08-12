#! /usr/bin/env python3


# description
GAME_RULE = 'Answer "yes" if the given number is prime, otherwise answer "no"'
PRIME_NUMBERS = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
MIN_NUM = PRIME_NUMBERS[0]
MAX_NUM = PRIME_NUMBERS[-1]


def get_question_answer(get_random_num) -> tuple:
    random_num = get_random_num(MIN_NUM, MAX_NUM)
    question = random_num
    answer = "yes" if random_num in PRIME_NUMBERS else "no"

    return (question, answer)


def init_game(get_random_num, GAME_DURATION: int) -> tuple:
    questions, answers = [None]*GAME_DURATION, [None]*GAME_DURATION
    for i in range(GAME_DURATION):
        questions[i], answers[i] = get_question_answer(get_random_num)

    return (GAME_RULE, questions, answers)
