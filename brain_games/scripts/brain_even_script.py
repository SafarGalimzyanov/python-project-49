import brain_games.games.brain_even as b_even


def main():
    game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    min_num = 1
    max_num = 21  # range for randrange is 1 - 20
    
    b_even.init_game(game_rule, min_num, max_num)


if __name__ == '__main__':
    main()
