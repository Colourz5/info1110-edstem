import sys
import math


def nCr(n, r):
    f = math.factorial
    number = f(n) / f(r) / f(n-r)
    number = int(round(number))
    return number


def pascalrow(n):
    column_number = n
    pascal_list = []
    for k in range(0, column_number + 1):
        number = nCr(n, k)
        pascal_list.append(number)
    print(*pascal_list)


try:
    row_number = int(sys.argv[1])
except ValueError:
    print("Invalid argument.")
    sys.exit()
except IndexError:
    print("Not enough arguments.")
    sys.exit()
if len(sys.argv) > 2:
    print("Too many arguments.")
    sys.exit()

for n in range(row_number + 1):
    pascalrow(n)
