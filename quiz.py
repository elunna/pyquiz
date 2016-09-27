import random

MAX_GUESSES = 3


class Quiz():
    def __init__(self, filename=None, qty=10):
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
        return len(self.quiz)

    def __next__(self):
        if self.counter >= self.qty:
            raise StopIteration()
        elif self.move_on:
            self.counter += 1
            self.move_on = False

        return self.question()

    def __iter__(self):
        return self

    def __str__(self):
        print('Game in progress? {}'.format(self.move_on))
        print('Questions: {}'.format(len(self)))
        print('Solved: {}'.format(self.solved))
        print('Failed: {}'.format(len(self.failed)))
        print('Guesses: {}'.format(self.guesses))
        print('Accuracy: {}%'.format(self.accuracy()))

    def accuracy(self):
        return round((self.solved / self.guesses) * 100, 2)

    def show(self):
        """
        Show all questions and answers in the quiz.
        """
        return self.print_db(self.quiz)

    def show_failed(self):
        return self.print_db(self.failed)

    def print_db(self, db):
        _str = ''
        for k, v in db:
            for item in v:
                _str += '{} --> {}\n'.format(k, item)
        return _str

    def question(self):
        return self.test[self.counter]

    def answers(self):
        return self.quiz[self.test[self.counter]]

    def reset_attempts(self):
        self.guesses += self.attempts
        self.attempts = 0
        self.move_on = True

    def check_guess(self, guess):
        """
        Checks the user guess against the valid answers. Returns True if the answer matches a valid
        answer.
        """
        # Make sure that case does not matter. Check all as lowercase.
        self.attempts += 1

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

                db[question] = answers
        return db
