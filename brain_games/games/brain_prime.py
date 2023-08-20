from math import sqrt


# description
GAME_RULE = 'Answer "yes" if the given number is prime, otherwise answer "no"'
MIN_NUM = 1
MAX_NUM = 99


def is_prime(n: int) -> bool:
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def get_question_answer(get_random_num) -> tuple:
    def inner():
        random_num = get_random_num(MIN_NUM, MAX_NUM)
        question = random_num
        answer = "yes" if is_prime(question) else "no"

        return (question, answer)
    return inner
