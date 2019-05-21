import sys

try:
    numbers = input("Enter two numbers: ")
    num_list = numbers.split()
    for i in range(len(num_list)):
        num_list[i] = float(num_list[i])
    a = num_list[0]
    b = num_list[1]
    equation1 = (a + b)/a
    equation2 = a/b
    if round(equation1, 3) == round(equation2, 3):
        print("\nGolden ratio!")
    else:
        equation1 = (a + b)/b
        equation2 = b/a
        if round(equation1, 3) == round(equation2, 3):
            print("\nGolden ratio!")
        else:
            print("\nMaybe next time.")
except ValueError or IndexError:
    print("\nInvalid input.")
    sys.exit()
