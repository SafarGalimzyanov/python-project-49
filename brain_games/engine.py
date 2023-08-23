from prompt import string


GAME_DURATION = 3  # the game ends after 3 correct answers in a row


def play_game(GAME_RULE: str, GetQuestionAnswer) -> None:
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!\n{GAME_RULE}')

    for _ in range(GAME_DURATION):
        question, right_answer = GetQuestionAnswer()
        print(f'Question: {question}')
        user_answer = string('Your answer: ')

        if user_answer != right_answer:  # exit
            print(f'"{user_answer}" is a wrong answer ;(', end='')
            print(f'Correct answer was "{right_answer}".')
            print(f"Let's try again, {user_name}!")
            return

        print('Correct!')
    print(f'Congratulations, {user_name}!')
