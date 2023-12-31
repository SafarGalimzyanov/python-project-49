from brain_games.games.utils import get_random_num
from typing import Tuple


# description
GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 99


def get_question_answer() -> Tuple[str, str]:
    random_num = get_random_num(MIN_NUM, MAX_NUM)

    question = random_num
    answer = 'yes' if random_num % 2 == 0 else 'no'

    return (question, answer)
