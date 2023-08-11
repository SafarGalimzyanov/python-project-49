#! /usr/bin/env python3


from brain_games.engine import GAME_DURATION, get_random_num
from math import gcd


# description
GAME_RULE = 'Find the greatest common divisor of the given numbers'
MIN_NUM = 1
MAX_NUM = 99


def get_question_answer() -> tuple:
    left_random_num = get_random_num(MIN_NUM, MAX_NUM)
    right_random_num = get_random_num(MIN_NUM, MAX_NUM)
    question = f'{left_random_num} {right_random_num}'
    answer = str(gcd(left_random_num, right_random_num))

    return (question, answer)
    

def init_game() -> tuple:
    questions, answers = [None]*GAME_DURATION, [None]*GAME_DURATION
    for i in range(GAME_DURATION):
        questions[i], answers[i] = get_question_answer()
    
    return (GAME_RULE, questions, answers)


if __name__ == '__main__':
    main()
