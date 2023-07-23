#! /usr/bin/env python3


import brain_games.games_logic as game
from random import choice


def main():
    game_rule = 'Answers "yes" if the given numbers is prime, otherwise answers "no"'

    questions_num = 3
    max_num = 100
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    questions = []
    right_answers = []

    for _ in range(questions_num):
        ran_num = choice(range(1, 100))
        questions.append(ran_num)
        right_answers.append('yes' if ran_num in prime_numbers else 'no')
    
    game.play_game(game_rule, questions, right_answers)



if __name__ == '__main__':
    main()
