from prompt import string


def play_game(game_rule: str, game_questions: list, right_answers: list):
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ') #prompt
    print(f'Hello, {user_name}!')
    print(f'{game_rule}')


    count = 0 #count of correct answers = number of questions = length of /questions list/ and /right_answers list/
    while count < 3: #the game ends after three correct answers
        print(f'Question: {game_questions[count]}')
        user_answer = string('Your answer: ') #prompt
        
        if user_answer == right_answers[count]:
            print('Correct!')
            count += 1
        else: #the game finishes with a failure
            print(f'{user_answer} is a wrong answer ;(. Correct answer was "{right_answers[count]}".\nLet`s try again, {user_name}!')
            return
    

    print(f'Congratulations, {user_name}!') #the user was correct 3 times in a row
