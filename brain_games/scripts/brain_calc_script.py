import brain_games.games.brain_calc as b_calc


def main():
    game_rule = 'What is the result of the expression?'  # description of the game
    viable_operators = ('+', '-', '*')  # the operands the user to interacts with
    max_operand = 21  # the biggest number the user to interacts with
    
    b_calc.init_game(game_rule, viable_operators, max_operand)

    
if __name__ == '__main__':
    main()
