# description
GAME_RULE = 'What is the result of the expression?'
MIN_NUM = 1
MAX_NUM = 20
VIABLE_OPERATORS = ('+', '-', '*')


def get_question_answer(get_random_num, get_random_elem) -> tuple:
    def inner():
        left_operand = get_random_num(MIN_NUM, MAX_NUM)
        right_operand = get_random_num(MIN_NUM, MAX_NUM)
        operator = get_random_elem(VIABLE_OPERATORS)

        question = (f'{left_operand} {operator} {right_operand}')

        match operator:
            case '+':
                answer = str(left_operand + right_operand)
            case '-':
                answer = str(left_operand - right_operand)
            case'*':
                answer = str(left_operand * right_operand)

        return (question, answer)
    return inner
