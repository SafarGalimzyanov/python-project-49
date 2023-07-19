#!/usr/bin/env python3

import brain_games.games_logic as game
from random import randrange


def main():
    game_rule = 'Answer "yes" if the number is even, otherwise answer "no"'
    
    max_number = 21 #range for randrange is 1 - 20
    questions_num = 3 #number of questions to answer
    questions = []
    right_answers = [] #"yes" if even, "no" if odd
    for _ in range(questions_num):
        rand_num = randrange(1, max_number)
        questions.append(rand_num)
        right_answers.append('yes' if rand_num % 2 == 0 else 'no')

    game.play_game(game_rule, questions, right_answers)


if __name__ == '__main__':
    main()
