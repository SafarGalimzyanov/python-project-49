#! /usr/bin/env python3


import brain_games.user_interaction as u_i
from random import choice


def main():
   questions = []
    right_answers = []

    for _ in range(game.GAME_DURATION):
        ran_num = choice(range(min_num, max_num))
        questions.append(ran_num)
        right_answers.append('yes' if ran_num in PRIME_NUMBERS else 'no')

    game.play_game(game_rule, questions, right_answers)


if __name__ == '__main__':
    main()
