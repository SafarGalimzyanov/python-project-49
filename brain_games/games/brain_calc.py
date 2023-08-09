#!/usr/bin/env python3

import brain_games.user_interaction as u_i
from random import randrange, choice


def get_questions_answers(left_operands: list, operators: list, right_operands: list) -> tuple:
    questions = []
    right_answers = []
    for i in range(u_i.GAME_DURATION):
        questions.append(f'{left_operands[i]} {operators[i]} {right_operands[i]}')
        match operators[i]:
            case '+':
                right_answers.append(str(left_operands[i] + right_operands[i]))
            case '-':
                right_answers.append(str(left_operands[i] - right_operands[i]))
            case'*':
                right_answers.append(str(left_operands[i] * right_operands[i]))

    return (tuple(questions), tuple(right_answers))


def get_random_operands(max_operand: int) -> tuple:
    left_operands = []
    right_operands = []
    for _ in range(u_i.GAME_DURATION):
        left_operands.append(int(randrange(max_operand)))
        right_operands.append(int(randrange(max_operand)))

    return (tuple(left_operands), tuple(right_operands))


def get_random_operators(viable_operators: tuple) -> tuple:
    operators = []
    for _ in range(u_i.GAME_DURATION):
        operators.append(choice(viable_operators))

    return tuple(operators)


def init_game(game_rule: str, viable_operators: tuple, max_operand: int) -> None:
    left_operands, right_operands = get_random_operands(max_operand)
    operators = get_random_operators(viable_operators)
    questions, right_answers = get_questions_answers(left_operands, viable_operators, right_operands)
    u_i.play_game(game_rule, questions, right_answers)
