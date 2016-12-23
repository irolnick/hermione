from Operators import operator_shapes


class Question:

    def __init__(self, num1, operator, num2, result, multiple_choice=None):
        if multiple_choice is None:
            multiple_choice = []
        self.num1 = num1
        self.num2 = num2
        self.operator = operator
        self.result = result
        self.multiple_choice = multiple_choice

    def __str__(self):
        output = "{} {} {} = {}\n".format(self.num1, operator_shapes[self.operator], self.num2, "")
        for choice in self.multiple_choice:
            output = "{}{}\t{}\n".format(output,  choice[0], choice[1])
        return output
