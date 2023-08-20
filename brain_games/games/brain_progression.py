# description
GAME_RULE = 'What number is missing in the progression?'
MIN_START = 0
MIN_STEP = 1
DEVIATION = 9
PROGRESSION_LENGTH = 10


def get_progression(start: int, step: int, length: int) -> list:
    return [str(start + step*i) for i in range(length)]


def get_question_answer(get_random_num, get_random_elem) -> tuple:
    def inner():
        start = get_random_num(MIN_START, MIN_START*DEVIATION)
        step = get_random_num(MIN_STEP, MIN_STEP*DEVIATION)
        question = get_progression(start, step, PROGRESSION_LENGTH)
        hide_elem, hide_elem_index = get_random_elem(question, index=True)
        answer = hide_elem
        question[hide_elem_index] = '..'

        return (question, answer)
    return inner
