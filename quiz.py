import random

MAX_GUESSES = 3


class Quiz():
    def __init__(self, filename=None, qty=10):
        """
        Initialize a new test from the flatfile specified by the database filename. If we don't
        get a filename, we cannot create the quiz.
        """
        if filename:
            self.quiz = self.import_db(filename)
        else:
            raise ValueError('Need a filename to import the quiz database!')

        self.name = filename
        self.solved = 0
        self.guesses = 0
        self.attempts = 0  # Guess attempts on the current question
        self.failed = {}

        if qty > len(self.quiz):
            self.qty = len(self.quiz)
        else:
            self.qty = qty

        self.move_on = False  # Flag for moving on from the current question
        self.counter = 0

        questions = list(self.quiz.keys())
        random.shuffle(questions)
        self.test = questions[0:self.qty]

    def __len__(self):
        """
        Return how many questions are in the entire quiz.
        """
        return len(self.quiz)

    def __next__(self):
        """
        Retrieve the next question in the randomly generated quiz. Only get the next question if
        we have not completed the current question.
        """
        if self.counter >= self.qty:
            raise StopIteration()
            return None
        elif self.move_on:
            self.counter += 1
            self.move_on = False

        return self.question()

    def __iter__(self):
        """
        Returns the iterator for this quiz.
        """
        return self

    def __str__(self):
        """
        Shows the statistics on the current quiz in progress.
        """
        _str = ''
        _str += 'Game in progress? {}'.format(self.move_on)
        _str += 'Questions: {}'.format(len(self))
        _str += 'Solved: {}'.format(self.solved)
        _str += 'Failed: {}'.format(len(self.failed))
        _str += 'Guesses: {}'.format(self.guesses)
        _str += 'Accuracy: {}%'.format(self.accuracy())
        return _str

    def accuracy(self):
        """
        Returns how accurate the players guesses have been so far in this quiz.
        """
        return round((self.solved / self.guesses) * 100, 2)

    def show_all(self):
        """
        Show all questions and answers in the quiz.
        """
        return self.print_db(self.quiz)

    def show_failed(self):
        """
        Show what questions the player has failed in this quiz.
        """
        return self.print_db(self.failed)

    def print_db(self, db):
        """
        Print out the set of questions and answers in the specified quiz dictionary.
        """
        _str = ''
        for k, v in db.items():
            for item in v:
                _str += '{} --> {}\n'.format(k, item)
        return _str

    def question(self):
        """
        Returns the current question as a string.
        """
        return self.test[self.counter]

    def answers(self):
        """
        Returns the answers to the current question as a list.
        """
        return self.quiz[self.test[self.counter]]

    def reset_attempts(self):
        """
        Adds the number of attempts at the current question to the total guesses and resets the
        attempts to 0. Sets the move_on boolean to True so we can move on to the next question.
        """
        self.guesses += self.attempts
        self.attempts = 0
        self.move_on = True

    def check_guess(self, guess):
        """
        Checks the user guess against the valid answers. Returns True if the answer matches a
        valid answer, returns False if the answer does not match.

        The user only gets a set number of guesses, as specified by the MAX_GUESSES global. If
        they go over this limit, we move on to the next question and add the question to the
        failed list.
        """
        self.attempts += 1

        # Make sure that case does not matter. Check all as lowercase.
        if guess.lower() in [a.lower() for a in self.answers()]:
            self.solved += 1
            self.reset_attempts()
            return True
        elif self.attempts == MAX_GUESSES:
            self.failed[self.question()] = self.answers()
            self.reset_attempts()
            return False
        else:
            return False

    def import_db(self, filename):
        """
        Parses through the db_file(which is a text file) and creates a dictionary of QUESTIONS and
        ANSWERS, where ANSWERS is a list of possible strings that are acceptable.
        """
        DELIMITER = '::'
        db = {}
        with open(filename) as quizfile:
            for line in quizfile.readlines():
                # Strip the blank spaces from the ends of all terms.
                terms = [t.strip() for t in line.split(DELIMITER)]
                question = terms[0]
                answers = [t for t in terms[1:] if t != '']

                # Ignore empty questions or answers.
                if question == '' or len(answers) < 1:
                    continue

                #  db[question] = answers  # Writes over existing answers.
                for a in answers:
                    db.setdefault(question, set()).add(a)
        return db
