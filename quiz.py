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


def guess(answer, question):
    """
    Print the question (or relative definition, etc) and lets the user have 3 guesses to get the
    correct term.
    """
    print('-'*20)
    attempts = 0
    while attempts < 3:
        guess = input('> ')
        attempts += 1

        if guess.lower() == answer.lower():
            print('Correct!\n')
            return attempts
        else:
            print('Wrong!\n')

    print('The correct answer is: {}'.format(answer))
    #  print('We\'ll try the next question...\n')
    return -1


def test_keys(user, test_dict):
    for k, v in test_dict.items():
        print('{}'.format(v))
        result = guess(k, v)
        if result > 0:
            user.solved += 1
            user.guesses += result
        else:
            user.guesses += 3


def test_values(test_dict):
    for k, v in test_dict.items():
        print('{}?'.format(k))
        guess(v, k)


def is_valid_entry(termdef):
    if len(termdef) != 2:
        return False

    if len(termdef[0]) == 0 or len(termdef[1]) == 0:
        return False

    return True  # It passed all the tests


def import_db(filename):
    """
    Parses through the db_file(which is a text file) and creates a dictionary of QUESTIONS and
    ANSWERS, where ANSWERS is a list of possible strings that are acceptable.
    """
    try:
        wordfile = open(filename)
    except:
        print("Something is wrong with the filename. Exiting!")
        exit()

    db = {}
    skippedlines = 0
    for line in wordfile.readlines():
        words = line.split('::')
        if is_valid_entry(words):
            db[words[0].strip()] = [words[1].strip()]
        else:
            pass
            # print('There is something wrong with the line, skipping...')
            skippedlines += 1
    print('Skipped {} lines while importing the database.'.format(skippedlines))
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
    print()
    print("The available topics are...")
    quizlist = [f for f in os.listdir('.') if os.path.isfile(f) and str(f).endswith('.quiz')]
    for i, quiz in enumerate(quizlist):
        print('\t{}\t{}'.format(i, quiz))

    while True:
        print('Enter the file you want to work with:')
        print()
        menunum = input('> ')
        try:
            menunum = int(menunum)
            if menunum in range(len(quizlist)):
                return quizlist[menunum]
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

    # check if they have a file
    try:
        with open(userfile, 'rb') as f:
            print('This user has a file that exists')
            print('Loading the players info...')
            user = pickle.load(f)
            return user

    except IOError:
        print("This user doesn't seem to have an account.")
        print('You are starting a new game eh? Well good luck!')
        return player.Player(name)


def display_user(user):
    """
    Displays the player's information
    """
    print('Type of user is {}'.format(type(user)))
    print('user is {}'.format(user.name))
    print('score is {}'.format(user.solved))
    print('guesses is {}'.format(user.guesses))


def save_user(user):
    """
    Saves the players current stats to file.
    """
    userfile = user.name + '.dat'
    print('Saving your data to file')

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
    display_user(user)

    quiz = choose_quiz()

    print('You chose the {} file!.'.format(quiz))
    cmds = import_db(quiz)

    # display_database(cmds)

    print('Beginning the quiz!!!\n\n')
    qty = 10
    testset = make_test_set(cmds, qty)

    test_keys(user, testset)
    # os.system('clear')

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
