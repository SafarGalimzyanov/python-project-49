from math import gcd
from brain_games.games.utils import get_random_num
from typing import Tuple


# description
GAME_RULE = 'Find the greatest common divisor of the given numbers.'
MIN_NUM = 1
MAX_NUM = 99


def get_question_answer() -> Tuple[str, str]:
    left_random_num = get_random_num(MIN_NUM, MAX_NUM)
    right_random_num = get_random_num(MIN_NUM, MAX_NUM)

    question = f'{left_random_num} {right_random_num}'
    answer = str(gcd(left_random_num, right_random_num))

    return (question, answer)
