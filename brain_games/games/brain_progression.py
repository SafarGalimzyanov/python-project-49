#! /usr/bin/env python3


from brain_games.engine import GAME_DURATION, get_random_num


# description
GAME_RULE = 'What number is missing in the progression?'
START_NUM = 1
MIN_STEP = 1
MAX_STEP = 6
MIN_INDEX = 0
PROGRESSION_LENGTH = 20


def get_question_answer() -> tuple:
    progression = []
    step = get_random_num(MIN_STEP, MAX_STEP)
    elem_to_hide = get_random_num(MIN_INDEX, PROGRESSION_LENGTH)
    for i in range(PROGRESSION_LENGTH):
        progression.append(str(START_NUM + step*i))

    question = progression
    answer = progression[elem_to_hide]
    progression[elem_to_hide] = '..'
    
    return (question, answer)


def init_game() -> tuple:
    questions, answers = [None]*GAME_DURATION, [None]*GAME_DURATION
    for i in range(GAME_DURATION):
        questions[i], answers[i] = get_question_answer()

    return (GAME_RULE, questions, answers)
