# Returns decimal representation of given binary number.
def to_decimal(b):
    integer = 0
    exponent = 0
    for i in range(-1, -(len(b) + 1), -1):
        integer += 2**(exponent) * int(b[i])
        exponent += 1
    return integer


# Returns whether or not given string is a binary number.
def is_binary(b):
    b = b.replace("0", "").replace("1", "")
    if b == "":
        return True
    else:
        return False


binary = input("Enter binary: ")
if is_binary(binary):
    binary = to_decimal(binary)
    print("\n{} in decimal".format(binary))
else:
    print("\nNot binary!")
