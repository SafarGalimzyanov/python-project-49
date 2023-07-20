#! /usr/bin/env python3

import brain_games.games_logic as game
from random import randrange
from math import gcd

def main():
    
    game_rule = 'Find the greates common divisor of given numbers'

    questions_num = 3

    left_nums = []
    right_nums = []
    for _ in range(questions_num):
        left_nums.append(randrange(1, 100))
        right_nums.append(randrange(1, 100))


    questions = []
    right_answers = []
    for i in range(questions_num):
        questions.append(f'{left_nums[i]} {right_nums[i]}')
        right_answers.append(str(gcd(left_nums[i], right_nums[i])))


    game.play_game(game_rule, questions, right_answers)


if __name__ == '__main__':
    main()
