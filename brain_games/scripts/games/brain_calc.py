#!/usr/bin/env python3


import brain_games.games_logic as game
from random import randrange, choice


def main():
    game_rule = 'What is the result of the expression?'

    viable_operands = ['+', '-', '*']
    max_num = 21
    left_nums = []
    operands = []
    right_nums = []
    for _ in range(game.GAME_DURATION):
        left_nums.append(randrange(max_num))
        operands.append(choice(viable_operands))
        right_nums.append(randrange(max_num))

    questions = []
    right_answers = []
    for i in range(game.GAME_DURATION):
        questions.append(f'{left_nums[i]} {operands[i]} {right_nums[i]}')
        match operands[i]:
            case '+':
                right_answers.append(str(int(left_nums[i]) + int(right_nums[i])))
            case '-':
                right_answers.append(str(int(left_nums[i]) - int(right_nums[i])))
            case'*':
                right_answers.append(str(int(left_nums[i]) * int(right_nums[i])))

    game.play_game(game_rule, questions, right_answers)


if __name__ == '__main__':
    main()
