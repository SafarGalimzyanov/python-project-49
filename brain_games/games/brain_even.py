#!/usr/bin/env python3

import brain_games.user_interaction as u_i
from random import randrange


def get_questions_answers(min_num: int, max_num: int) -> tuple:
    questions = []
    right_answers = []
    for _ in range(u_i.GAME_DURATION):
        rand_num = get_random_num(min_num, max_num)
        questions.append(rand_num)
        right_answers.append('yes' if rand_num % 2 == 0 else 'no')

    return (tuple(questions), tuple(right_answers))


def get_random_num(min_num: int, max_num: int) -> int:
    return randrange(min_num, max_num)


def init_game(game_rule: str, min_num: int, max_num: int) -> None:
    questions, answers = get_questions_answers(min_num, max_num)
    u_i.play_game(game_rule, questions, answers)


if __name__ == '__main__':
    main()
