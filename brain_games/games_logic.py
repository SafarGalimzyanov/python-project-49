from prompt import string


GAME_DURATION = 3  # the game ends after 3 correct answers in a row


def play_game(game_rule: str, game_questions: list, right_answers: list):
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(f'{game_rule}')

    for i in range(GAME_DURATION):
        print(f'Question: {game_questions[i]}')
        user_answer = string('Your answer: ')

        if user_answer == right_answers[i]:  # continue
            print('Correct!')
        else:  # exit
            print(f'"{user_answer}" is a wrong answer ;(. Correct answer was "{right_answers[i]}".')
            print(f'Let`s try again, Tirion!')
            return

    print(f'Congratulations, {user_name}!')
