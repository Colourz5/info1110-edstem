import sys


def draw_triangle_segment(height):
    image = []
    for count in range(1, height + 1):
        trail = height - count
        row = trail * " " + "/" + 2 * (count - 1) * " " + "\\"
        row += trail * " "
        image.append(row)
    image[-1] = image[-1].replace(" ", "_")
    return image


def defaultdraw(image, height):
    for row in image:
        print(height * " ", end="")
        print(row.rstrip())
    for row in image:
        print(row, end="")
        print(row.rstrip())


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
defaultdraw(draw_triangle_segment(HEIGHT), HEIGHT)
