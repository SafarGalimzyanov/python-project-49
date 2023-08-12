from brain_games.games.brain_progression import init_game
from brain_games.engine import GAME_DURATION, play_game, get_random_num, get_random_elem


def main():
    play_game(*init_game(get_random_num, get_random_elem, GAME_DURATION))


if __name__ == '__main__':
    main()
