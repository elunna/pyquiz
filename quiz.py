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
import random


def display_db(quiz):
    """
    Show all questions and answers in the quiz.
    """
    _str = ''
    for k, v in quiz.items():
        for item in v:
            _str += '{} --> {}\n'.format(k, item)
    return _str


def check_guess(answers, guess):
    """
    Checks the user guess against the valid answers. Returns True if the answer matches a valid
    answer.
    """
    # Make sure that case does not matter. Check all as lowercase.
    if guess.lower() in [a.lower() for a in answers]:
        return True
    else:
        return False


def guess(question, answer):
    """
    Print the question (or relative definition, etc) and lets the user have 3 guesses to get the
    correct term.
    """
    attempts = 0
    while attempts < 3:
        guess = input('> ')
        attempts += 1

        if check_guess(answer, guess):
            print('Correct!\n')
            return attempts
        else:
            print('Wrong!\n')

    print('The correct answer is: {}'.format(answer))
    return -1


def test(user, quiz):
    """
    Execute a test of the quiz to the user.
    """
    failed = {}
    guesses = 0

    for question, answer in quiz.items():
        print('-'*40 + '-')
        print('{}'.format(question))
        result = guess(question, answer)
        if result > 0:
            user.solved += 1
            user.guesses += result
            guesses += result
        else:
            failed[question] = answer
            user.guesses += 3
            guesses += 3
    return failed, guesses


def import_db(filename):
    """
    Parses through the db_file(which is a text file) and creates a dictionary of QUESTIONS and
    ANSWERS, where ANSWERS is a list of possible strings that are acceptable.
    """
    # The standard quiz file delimiter is '::'
    delimiter = '::'
    db = {}
    with open(filename) as quizfile:
        for line in quizfile.readlines():
            # Strip the blank spaces from the ends of all terms.
            terms = [t.strip() for t in line.split(delimiter)]
            question = terms[0]
            answers = [t for t in terms[1:] if t != '']

            # Ignore empty questions or answers.
            if question == '' or len(answers) < 1:
                continue

            # Allow questions to have multiple answers on multiple lines in the quiz file.
            if question in db:
                for a in answers:
                    if a in db[question]:
                        pass
                    else:
                        db[question].append(a)
            else:
                db[question] = answers
    return db


def make_test_set(db, quantity):
    """
    Takes a (presumably large) database and extracts the specified number of term/def pairs.
    """
    keylist = list(db.keys())
    random.shuffle(keylist)

    keylist = keylist[0:quantity]

    test_set = {}
    for key in keylist:
        test_set[key] = db.get(key)

    return test_set


def choose_quiz():
    """
    List all the .quiz files in the specified quiz directory.
    """
    FILEPATH = './quiz/'
    print("\nThe available topics are...")

    quizlist = [f for f in os.listdir(FILEPATH) if str(f).endswith('.quiz')]

    for i, quiz in enumerate(quizlist):
        print('\t{}\t{}'.format(i, quiz))

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

    user = player.process_user()
    filename = choose_quiz()
    quiz = import_db(filename)

    print('This quiz has {} questions...'.format(len(quiz)))
    print('Beginning the quiz!!!\n\n')

    failed, guesses = test(user, quiz)
    solved = len(quiz) - len(failed)
    accuracy = round((solved / guesses) * 100, 2)

    # SUMMARY
    print('#'*80)
    print('='*80)
    print('Showing your stats...')
    print('-'*80)
    print(filename)
    print('Questions: {}'.format(len(quiz)))
    print('Solved: {}'.format(solved))
    print('Failed: {}'.format(len(failed)))
    print('Guesses: {}'.format(guesses))
    print('Accuracy: {}%'.format(accuracy))
    print()
    print('You got these incorrect:')
    for k, v in failed.items():
        print('Q:{} --> A: {}'.format(k, v))

    player.save_user(user)
