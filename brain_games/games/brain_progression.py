#! /usr/bin/env python3


# description
GAME_RULE = 'What number is missing in the progression?'
START_NUM = 1
MIN_STEP = 1
MAX_STEP = 6
MIN_INDEX = 0
PROGRESSION_LENGTH = 20


def get_question_answer(get_random_num, get_random_elem) -> tuple:
    question = []
    step = get_random_num(MIN_STEP, MAX_STEP)
    for i in range(PROGRESSION_LENGTH):
        question.append(str(START_NUM + step*i))

    elem, elem_index = get_random_elem(question, index=True)
    answer = elem
    question[elem_index] = '..'

    return (question, answer)


def init_game(get_random_num, get_random_elem, GAME_DURATION: int) -> tuple:
    questions, answers = [None]*GAME_DURATION, [None]*GAME_DURATION
    for i in range(GAME_DURATION):
        questions[i], answers[i] = get_question_answer(get_random_num, get_random_elem)

    return (GAME_RULE, questions, answers)
