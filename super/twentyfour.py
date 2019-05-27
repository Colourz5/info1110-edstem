import sys
from itertools import permutations
from itertools import product
# YOU HAVE TO USE BRACKETS ARGGHHH


def check(num_perms, op_perms, TARGET):
    for numbers in num_perms:
        for operators in op_perms:
            expression = "{} {} {} {} {} {} {}".format(numbers[0], operators[0], numbers[1], operators[1], numbers[2], operators[2], numbers[3])
            result = eval(expression)
            if result == TARGET:
                return True
    return False


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