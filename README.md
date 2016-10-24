# PyQuiz

This is a Python program to test a student using flashcard-like quizzes. By 
making a text file of questions and answers, you can easily make quizzes and test
yourself on school notes, test terms, new business terminology, and so on. 

The quiz files are listed out in the /quiz/ directory.
The quizzes are listed out in this format:
* Question :: Answer1

! Note that each quiz file needs to end in .quiz.

```
testquiz.quiz
What is the question? :: This is the answer
Who is that? :: This is me
```

The text file can contain multiple answers for a question
```
testquiz2.quiz
What is furry and has four legs and meows? :: Cat :: Kitten
What has four legs and barks? :: Dog :: Puppy :: Canine
```

### Prerequisities
Python 3

### Running
```
$ python3 quiz.py
```

## Running the tests
```
$ python3 -m unittest discover
```

## Included
I have included a handful of quizzes that I created - most are for studying Linux commands, and 
CompTIA certification, and a few other miscellaneous quizzes for your entertainment. Enjoy!

## Authors

* **Erik Lunna**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
