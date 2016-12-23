import random
import math
import string
import sys

from Operators import *
from Question import *


def random_letter_but(exclude=""):
    chosen = string.upper(random.choice(string.ascii_letters + "_"))
    if chosen != exclude:
        return chosen
    else:
        return random_letter_but(exclude)


def random_int_but(exclude, max_int):
    chosen = random.randint(0, max_int)
    if chosen != exclude:
        return chosen
    else:
        return random_int_but(exclude, max_int)


def obtain_quiz_answer():
    return string.upper("predicting the future is a very difficult business indeed")


def obtain_multiple_choice(correct_answer, correct_result, max_number, num_choices):
    """ e.g.  if correct_answer = 'n'
                 correct_result = 12
                 max_number = 100
                 num_choices = 4
                 then the function will generate one candidate, which is the correct one: (12, n)
                 and num_choices - 1 = 3 candidates which are wrong answers, i.e. not 12, smaller than max_number (=100)
    """
    multiple_choice = [(correct_result, correct_answer)]
    for i in range(1, num_choices):
        multiple_choice.append((random_int_but(correct_result, max_number), random_letter_but(correct_answer)))
    random.shuffle(multiple_choice)
    return multiple_choice


def obtain_questions(answer, max_number=200, operators=None):
    if operators is None:
        operators = [Operators.MULTIPLICATION, Operators.DIVISION, Operators.ADDITION, Operators.SUBTRACTION]
    questions = []

    for letter in answer:
        # choose operator
        operator = random.choice(operators)

        # o1 * o2 = r
        if operator in OperatorFamilies.MULTIPLICATIVE:
            o1 = random.randint(0, math.floor(math.sqrt(max_number)))
            o2 = random.randint(0, math.floor(math.sqrt(max_number)))
            r = o1 * o2

            while operator == Operators.DIVISION and o1 == 0:
                o1 = random.randint(0, math.floor(math.sqrt(max_number)))

        # o1 + o2 = r
        if operator in OperatorFamilies.ADDITIVE:
            r = random.randint(0, max_number)
            o1 = random.randint(0, r)
            o2 = r - o1

        if operator in OperatorFamilies.BIGGER:
            question = Question(o1, operator, o2, r)
        else:
            question = Question(r, operator, o1, o2)

        question.multiple_choice = obtain_multiple_choice(letter, question.result, max_number, 4)
        questions.append(question)
    return questions


def main():
    quiz_answer = obtain_quiz_answer()
    questions = obtain_questions(quiz_answer, max_number=120,
                                 operators=[Operators.MULTIPLICATION, Operators.ADDITION, Operators.DIVISION,
                                            Operators.SUBTRACTION])
    for q in questions:
        print q
        print "\n"

    for _ in quiz_answer:
        sys.stdout.write("___   ")


if __name__ == "__main__":
    main()

