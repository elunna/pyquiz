#!/usr/bin/env python3
"""
Term and definition flashcard tester.

This program works with flat text files of term/definitions and is able to import them and
present the player with different sets of quizzes, analyze their answers, and provide useful
reports.

Text files of ANSWER/QUESTION pairs are imported and converted to dictionaries. The dictionary
keys are the answer

The text files have data stored as "ANSWER :: QUESTION"
-- Neither the ANSWER not the QUESTION can be empty
-- The ANSWER can contain numbers or be a number.
-- The QUESTION cannot contain numbers or non-english special characters.
-- Notice that a the data files can contain more than one QUESTION for an ANSWER, so that we can
take multiple answers. To accomodate multiple answers, whe
"""

from __future__ import print_function
import os
import player
import quiz


def test(q):
    """
    Execute a test of the quiz to the user.
    """
    for question in q:
        print('-'*40 + '-')
        print('{}'.format(question))
        guess = input('> ')

        if q.check_guess(guess):
            print('Correct!\n')
        else:
            print('Wrong!\n')


def choose_quiz():
    """
    List all the .quiz files in the specified quiz directory.
    """
    FILEPATH = './quiz/'
    print("\nThe available topics are...")

    quizlist = [f for f in os.listdir(FILEPATH) if str(f).endswith('.quiz')]

    for i, q in enumerate(quizlist):
        print('\t{}\t{}'.format(i, q))

    while True:
        print('\nPlease select the file number to work with:')
        menunum = input('> ')
        try:
            menunum = int(menunum)
            if menunum in range(len(quizlist)):
                return FILEPATH + quizlist[menunum]
            else:
                print('Not a value menu option! Try again.')
        except ValueError:
            print('Not a value menu option! Try again.')


if __name__ == "__main__":
    os.system('clear')
    print("Welcome to Erik's Python Quizinator!")

    while True:
        name = input('Please enter your name > ')
        user = player.load_player(name)
        if user is None:
            print('Do you want to create a new player?')
            choice = input('> ')
            if choice.lower().startswith('y'):
                user = player.Player(name=name)
                break
        else:
            break

    filename = choose_quiz()
    q = quiz.Quiz(filename)

    print('This quiz has {} questions...'.format(len(q)))
    print('Beginning the quiz!!!\n\n')

    test(q)

    # SUMMARY
    print('~'*80)
    print('Showing your stats...')
    str(q)
    print('~'*80)
    print(filename)
    print()
    print('You got these incorrect:')
    q.show_failed()

    player.save_user(user)
