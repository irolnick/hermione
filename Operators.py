# noinspection PyClassHasNoInit
class Operators:
    ADDITION = 1
    SUBTRACTION = 2
    MULTIPLICATION = 3
    DIVISION = 4


# noinspection PyClassHasNoInit
class OperatorFamilies:
    BIGGER = [Operators.ADDITION, Operators.MULTIPLICATION]
    SMALLER = [Operators.SUBTRACTION, Operators.DIVISION]
    ADDITIVE = [Operators.ADDITION, Operators.SUBTRACTION]
    MULTIPLICATIVE = [Operators.MULTIPLICATION, Operators.DIVISION]


operator_shapes = {Operators.ADDITION: "+", Operators.SUBTRACTION: "-", Operators.MULTIPLICATION: "x",
                   Operators.DIVISION: ":"}
