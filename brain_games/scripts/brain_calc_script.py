from brain_games.games.brain_calc import init_game
from brain_games.engine import play_game


def main():
    play_game(*init_game())


if __name__ == '__main__':
    main()
