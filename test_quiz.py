import unittest
import quiz


class TestQuiz(unittest.TestCase):

    """
    Tests for __init__(self, filename=None, qty=10):
    """

    """
    Tests for __len__(self):
    """

    """
    Tests for __next__(self):
    """

    """
    Tests for __iter__(self):
    """

    """
    Tests for __str__(self):
    """

    """
    Tests for accuracy(self):
    """

    """
    Tests for show_all(self):
    """

    """
    Tests for show_failed(self):
    """

    """
    Tests for print_db(self, db):
    """

    """
    Tests for question(self):
    """

    """
    Tests for answers(self):
    """

    """
    Tests for reset_attempts(self):
    """

    """
    Tests for import_db(filename):
    """
    # Test importing a single question/answer pair.
    # The answer should be in a list.
    def test_importdb_1QA(self):
        q = quiz.Quiz('tests/test_1answer.quiz')
        expected = {'What is the meaning of life?': {'42'}}
        result = q.quiz
        self.assertEqual(expected, result)

    # Test importing a question with multiple answers
    def test_importdb_7QA(self):
        q = quiz.Quiz('tests/test_7answers.quiz')
        expected = {'Colors in the rainbow?':
                    {'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'}}
        result = q.quiz
        self.assertEqual(expected, result)

    # Import ignores a blank line
    def test_importdb_dupes_blanklines_noEmptyKeys(self):
        q = quiz.Quiz('tests/test_dupes.quiz')
        expected = False
        result = '' in q.quiz.keys()
        self.assertEqual(expected, result)

    # Importing an entry on separate lines adds to the dictionary
    def test_importdb_dupes_2answers_difflines_returnsbothvalues(self):
        q = quiz.Quiz('tests/test_dupes.quiz')
        expected = {'grey', 'gray'}
        result = q.quiz.get('White plus black?')
        self.assertEqual(expected, result)

    # Importing a duplicate question, with an existing answer, does nothing.
    def test_importdb_dupes_duplicateentry_answerremainsthesame(self):
        q = quiz.Quiz('tests/test_dupes.quiz')
        expected = {'4'}
        result = q.quiz.get('2 + 2')
        self.assertEqual(expected, result)

    # Test importing a variety of question/answers
    # A blank question(the first term) is ignored:
    def test_importdb_dupes_blankquestion_ignored(self):
        # this dictionary should have 3 normal entries
        q = quiz.Quiz('tests/test_errors.quiz')
        expected = 3
        result = len(q.quiz)
        self.assertEqual(expected, result)

    """
    Tests for display_db(quiz):
    """
    # Test displaying a single question/answer pair.
    def test_displaydb_1QA(self):
        q = quiz.Quiz('tests/test_1answer.quiz')
        expected = 'What is the meaning of life? --> 42\n'
        result = q.print_db(q.quiz)
        self.assertEqual(expected, result)

    """
    Tests for check_guess(self, guess):
    """
    # Test if a question with a single answer.
    def test_iscorrect_1QA_correct_returnsTrue(self):
        q = quiz.Quiz('tests/test_1answer.quiz')
        # question = 'What is the meaning of life?'
        expected = True
        result = q.check_guess('42')
        self.assertEqual(expected, result)

    def test_iscorrect_1QA_wrong_returnsFalse(self):
        q = quiz.Quiz('tests/test_1answer.quiz')
        # question = 'What is the meaning of life?'
        expected = False
        result = q.check_guess('0')
        self.assertEqual(expected, result)

    # Test if a question with multiple answers.
    def test_iscorrect_7QA_correctlowercase_returnsTrue(self):
        q = quiz.Quiz('tests/test_7answers.quiz')
        # question  = 'Colors in the rainbow?'
        expected = True
        result = q.check_guess('red')
        self.assertEqual(expected, result)

    def test_iscorrect_7QA_correctuppercase_returnsTrue(self):
        q = quiz.Quiz('tests/test_7answers.quiz')
        # question = 'Colors in the rainbow?'
        expected = True
        result = q.check_guess('BLUE')
        self.assertEqual(expected, result)

    def test_iscorrect_7QA_wrong_returnsFalse(self):
        q = quiz.Quiz('tests/test_7answers.quiz')
        #  question = 'Colors in the rainbow?'
        expected = False
        result = q.check_guess('Chrome')
        self.assertEqual(expected, result)
