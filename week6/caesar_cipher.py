import sys
import string


def rotate(line, key):
    return line[key:] + line[:key]


def caesar(line, key):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = upper.lower()

    upper_shift = rotate(upper, key)
    lower_shift = rotate(lower, key)

    shift1 = str.maketrans(upper, upper_shift)
    line = line.translate(shift1)
    shift2 = str.maketrans(lower, lower_shift)
    line = line.translate(shift2)
    return line


try:
    key = int(input("Enter key: "))
except ValueError:
    print("\nInvalid key!")
    sys.exit()
if key < 0 or key > 26:
    print("\nInvalid key!")
    sys.exit()
line = input("Enter line: ")
print()
print(caesar(line, key))
