import sys


def draw_Triangle(height):
    for i in range(height):
        if ((i + 1) % height) != 0:
            print((2*height - 1 - i)*" " + "/" + 2*i*" " + "\\")
        else:
            print((2*height - 1 - i)*" " + "/" + 2*i*"_" + "\\")
    j = height - 1
    for i in range(height):
        if ((i + 1) % height) != 0:
            print((height - 1 - i)*" " + "/" + 2*i*" " + "\\", end="")
            print(2*j*" " + "/" + 2*i*" " + "\\")
            j -= 1
        else:
            print((height - 1 - i)*" " + "/" + 2*i*"_" + "\\", end="")
            print("/" + 2*i*"_" + "\\")


HEIGHT = input("Enter height: ")
print()
try:
    HEIGHT = int(HEIGHT)
    if HEIGHT < 2 or HEIGHT > 20:
        print("Invalid height.")
        sys.exit()
except ValueError:
    print("Invalid height.")
    sys.exit()

# drawing each row
draw_Triangle(HEIGHT)
