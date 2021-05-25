
"""delimiters"""

delimiters = ["+", "-", "*", "/"]

"""end"""

number1 = input("entry number 1: ")

number2 = input("entry number 2: ")

operator = input("entry the operator (+ - * /): ")

try:
    number1_ = int(number1)
except ValueError:
    number1_ = "incorrect"

try:
    number2_ = int(number2)
except ValueError:
    number2_ = "incorrect"

if number1_ is "incorrect" or number2_ is "incorrect":
    print("invalid data type")

else:
    if operator in delimiters:
        if operator is "+":
            result = number1_ + number2_
            print(result)

        elif operator is "-":
            result = number1_ - number2_
            print(result)

        elif operator is "*":
            result = number1_ * number2_
            print(result)
        else:
            result = number1_ / number2_
            print(result)

    else:
        print("incorrect operator")
