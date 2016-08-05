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

"""
def guess(answer, question):
def test_keys(user, test_dict):
def test_values(test_dict):
def is_valid_entry(termdef):
def make_test_set(db, quantity):
def choose_quiz():
def process_user():
def display_user(user):
def save_user(user):
"""
