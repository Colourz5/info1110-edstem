import sys
from itertools import permutations
from itertools import product
import numpy as np
# Reducing 24 to one of the numbers
# Still requires brackets to work


def check(num_perms, op_perms, TARGET):
    promising = []
    for operators in op_perms:
        for numbers in num_perms:
            result = TARGET
            promise = []
            for index in range(len(operators)):
                expression = "{} {} {}".format(result, operators[index],
                                               numbers[index])
                result = eval(expression)
                promise.append(expression)
            if abs(result - float(numbers[-1])) < pow(10, -14):
                print(str(promising))
                return True
            elif abs(result - float(numbers[-1])) < 0.13:
                promising.append(promise)
    print(str(promising))
    return False


if __name__ == "__main__":
    TARGET = 24.0
    operators = ["+", "-", "/", "*"]
    user_input = input("Enter 4 integers: ")
    print()
    digits = user_input.split()
    try:
        if len(digits) != 4:
            raise ValueError
        for digit in digits:
            int(digit)
    except ValueError:
        print("Input must consist of 4 integers")
        sys.exit()

    num_perms = list(permutations(digits))
    op_perms = list(product(operators, repeat=3))
    digits = "{ " + ", ".join(digits) + " }"
    if check(num_perms, op_perms, TARGET):
        print("Yes! {} is reachable from {}".format(int(TARGET), digits))
    else:
        print("Noooo :( {} is unreachable from {}".format(int(TARGET), digits))
