import unittest
import quiz


class TestQuiz(unittest.TestCase):
    #########################################
    # Tests for import_db(filename):
    #########################################
    # Test importing a single question/answer pair.
    # The answer should be in a list.
    def test_importdb_1QA(self):
        expected = {'What is the meaning of life?': ['42']}
        result = quiz.import_db('tests/test_1answer.quiz')
        self.assertEqual(expected, result)

    # Test importing a question with multiple answers
    def test_importdb_7QA(self):
        expected = {'Colors in the rainbow?':
                    ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']}
        result = quiz.import_db('tests/test_7answers.quiz')
        self.assertEqual(expected, result)

    # Test importing a variety of question/answers

    #########################################
    # Tests for display_db(quiz):
    #########################################
    # Test displaying a single question/answer pair.
    def test_displaydb_1QA(self):
        expected = 'What is the meaning of life? --> 42\n'
        db = quiz.import_db('tests/test_1answer.quiz')
        result = quiz.display_db(db)
        self.assertEqual(expected, result)

    #########################################
    # Tests for is_correct(db, term, guess):
    #########################################
    # Test if a question with a single answer.
    def test_guess_1QA_correct_returnsTrue(self):
        expected = True
        db = quiz.import_db('tests/test_1answer.quiz')
        key = 'What is the meaning of life?'
        guess = '42'
        result = quiz.is_correct(db, key, guess)
        self.assertEqual(expected, result)

    def test_guess_1QA_wrong_returnsFalse(self):
        expected = False
        db = quiz.import_db('tests/test_1answer.quiz')
        key = 'What is the meaning of life?'
        guess = '0'
        result = quiz.is_correct(db, key, guess)
        self.assertEqual(expected, result)

    # Test if a question with multiple answers.
    def test_guess_7QA_correctlowercase_returnsTrue(self):
        expected = True
        db = quiz.import_db('tests/test_7answers.quiz')
        key = 'Colors in the rainbow?'
        guess = 'red'
        result = quiz.is_correct(db, key, guess)
        self.assertEqual(expected, result)

    def test_guess_7QA_correctuppercase_returnsTrue(self):
        expected = True
        db = quiz.import_db('tests/test_7answers.quiz')
        key = 'Colors in the rainbow?'
        guess = 'BLUE'
        result = quiz.is_correct(db, key, guess)
        self.assertEqual(expected, result)

    def test_guess_7QA_wrong_returnsFalse(self):
        expected = False
        db = quiz.import_db('tests/test_7answers.quiz')
        key = 'Colors in the rainbow?'
        guess = 'Chrome'
        result = quiz.is_correct(db, key, guess)
        self.assertEqual(expected, result)


"""
def test_keys(user, test_dict):
def test_values(test_dict):
def is_valid_entry(termdef):
def make_test_set(db, quantity):
def choose_quiz():
def process_user():
def display_user(user):
def save_user(user):
"""
