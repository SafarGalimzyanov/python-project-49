import prompt
from random import randrange


def even_game():
    name = prompt.string('May I have your name? ') #get a name of the user
    print(f'Hello, {name}!\nAnswer "yes" if the number is even, otherwise answer "no"')

    count = 0 #count of correct answers
    max_num = 21 #range of numbers in the game
    viable_answers = ('yes', 'no') #acceptable user`s answers
    while count < 3: #the game ends after three correct answers
        rand_num = randrange(1, max_num) 
        right_answer = viable_answers[rand_num % 2] #'yes' = even, 'no' = odd
        print(f'Question: {rand_num}')
        user_answer = prompt.string('Your answer: ')
        
        if user_answer in viable_answers and user_answer == right_answer:
            print('Correct!')
            count += 1
        else: #the game ends with a failure
            print(f'{user_answer} is a wrong answer ;(. Correct answer was "{right_answer}".\nLet`s try again, {name}!')
            return
    

    print(f'Congratulations, {name}!')
