from brain_games.games.brain_gcd import init_game
from brain_games.engine import GAME_DURATION, play_game, get_random_num


def main():
    play_game(*init_game(get_random_num, GAME_DURATION))


if __name__ == '__main__':
    main()
