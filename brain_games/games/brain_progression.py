# description
GAME_RULE = 'What number is missing in the progression?'
START_NUM = 1
MIN_STEP = 1
MAX_STEP = 6
MIN_INDEX = 0
PROGRESSION_LENGTH = 20


def get_question_answer(get_random_num, get_random_elem) -> tuple:
    def inner():
        question = []
        step = get_random_num(MIN_STEP, MAX_STEP)
        for i in range(PROGRESSION_LENGTH):
            question.append(str(START_NUM + step*i))

        elem, elem_index = get_random_elem(question, index=True)
        answer = elem
        question[elem_index] = '..'

        return (question, answer)
    return inner
