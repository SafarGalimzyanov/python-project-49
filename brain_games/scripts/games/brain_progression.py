#! /usr/bin/env python3

import brain_games.games_logic as game
from random import choice

def arith_prog(start, step, num_of_elems):
    progression = []
    step_to_hide = choice(range(num_of_elems))
    elem_to_hide = 0
    for i in range(num_of_elems):
        if i == step_to_hide:
            elem_to_hide = str(start + step*i)
            progression.append('..')
        else:
            progression.append(str(start + step*i))

    return (elem_to_hide, progression)


def main():
    game_rule = 'What number is missing in the progression?'

    questions_num = 3
    num_of_elems = 10
    questions = [None]*questions_num
    right_answers = [None]*questions_num
    for i in range(questions_num):
        start = choice(range(21))
        step = choice(range(1, 6))
        right_answers[i], questions[i] = arith_prog(start, step, num_of_elems)
    
    game.play_game(game_rule, questions, right_answers)

if __name__ == '__main__':
    main()
