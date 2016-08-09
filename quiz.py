#!/usr/bin/env python3
"""
Term and definition flashcard tester.

This program works with text files of term/definitions and is able to import them and present
the player with different sets of quizzes, analyze their answers, and provide useful reports.

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
import random
import os
import pickle
import player


def display_db(quiz):
    _str = ''
    for k, v in quiz.items():
        for item in v:
            _str += '{} --> {}\n'.format(k, item)
    return _str


def is_correct(answers, guess):
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
    print('-'*20)
    attempts = 0
    while attempts < 3:
        guess = input('> ')
        attempts += 1

        #  if guess.lower() == answer.lower():
        if is_correct(answer, guess):
            print('Correct!\n')
            return attempts
        else:
            print('Wrong!\n')

    print('The correct answer is: {}'.format(answer))
    #  print('We\'ll try the next question...\n')
    return -1


def test(user, quiz):
    for question, answer in quiz.items():
        print('{}'.format(question))
        result = guess(question, answer)
        if result > 0:
            user.solved += 1
            user.guesses += result
        else:
            user.guesses += 3


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
    Takes the(presumably large) database and extracts the specified number of term/def pairs.
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
    List all the .quiz files
    """
    filepath = './quiz/'
    print()
    print("The available topics are...")
    quizlist = [f for f in os.listdir(filepath) if str(f).endswith('.quiz')]

    for i, quiz in enumerate(quizlist):
        print('\t{}\t{}'.format(i, quiz))

    while True:
        print('\nPlease select the file number to work with:')
        menunum = input('> ')
        try:
            menunum = int(menunum)
            if menunum in range(len(quizlist)):
                return filepath + quizlist[menunum]
            else:
                print('Not a value menu option! Try again.')
        except ValueError:
            print('Not a value menu option! Try again.')


def process_user():
    """
    Gets the username, checks for any previous player info and loads the player. If no player
    file it creates a new one. Returns a Player object.
    """
    name = input('Please enter your name adventurous one > ')
    userfile = str(name) + '.dat'
    print('\n')
    # check if they have a file
    try:
        with open(userfile, 'rb') as f:
            print('Loading the player file...')
            user = pickle.load(f)
            return user

    except IOError:
        print('This user doesn\'t seem to have an account...')
        print('Creating a new player file.')
        return player.Player(name)


def display_user(user):
    """
    Displays the player's information
    """
    print('Showing data for {}'.format(user.name))
    print('Score: {}'.format(user.solved))
    print('Guesses: {}'.format(user.guesses))


def save_user(user):
    """
    Saves the players current stats to file.
    """
    userfile = user.name + '.dat'
    print('Saving player file... ')

    try:
        with open(userfile, 'wb') as f:
            pickle.dump(user, f)
    except IOError:
        print('An error occurred while writing, aborting program!')
        exit()


def main():
    os.system('clear')
    print("Welcome to Erik's Python Quizinator!")

    user = process_user()
    filename = choose_quiz()
    quiz = import_db(filename)

    print('Beginning the quiz!!!\n\n')
    #  qty = 10
    #  testset = make_test_set(cmds, qty)

    test(user, quiz)
    save_user(user)


if __name__ == "__main__":
    main()


# MIT License

# Copyright (c) [2016] [Erik S. Lunna]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
