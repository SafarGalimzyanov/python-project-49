#!/usr/bin/env python3


from brain_games.games.brain_gcd import GAME_RULE, get_question_answer
from brain_games.engine import play_game


def main():
    play_game(GAME_RULE, get_question_answer)


if __name__ == '__main__':
    main()
