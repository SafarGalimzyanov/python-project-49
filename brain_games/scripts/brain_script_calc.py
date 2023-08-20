#!/usr/bin/env python3


from brain_games.games.brain_calc import GAME_RULE, get_question_answer
from brain_games.engine import play_game, get_random_num, get_random_elem


def main():
    play_game(GAME_RULE, get_question_answer(get_random_num, get_random_elem))


if __name__ == '__main__':
    main()
