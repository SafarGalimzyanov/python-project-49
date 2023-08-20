# description
GAME_RULE = 'Answer "yes" if the given number is prime, otherwise answer "no"'
PRIME_NUMBERS = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
MIN_NUM = PRIME_NUMBERS[0]
MAX_NUM = PRIME_NUMBERS[-1]


def get_question_answer(get_random_num) -> tuple:
    def inner():
        random_num = get_random_num(MIN_NUM, MAX_NUM)
        question = random_num
        answer = "yes" if random_num in PRIME_NUMBERS else "no"

        return (question, answer)
    return inner
