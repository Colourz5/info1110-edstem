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
        print(row)


def draw(image, height, rows):
    offset = height * (rows - 1)
    row_num = 1
    while offset != -height:
        for row in image:
            print(offset * " ", end="")
            for iteration in range(row_num):
                if iteration == row_num - 1:
                    print(row.rstrip())
                else:
                    print(row, end="")
        offset -= height
        row_num += 1


try:
    height = int(input("Enter height: "))
    if height < 1 or height > 20:
        raise ValueError
except ValueError:
    print("\nInvalid height.")
    sys.exit()
try:
    rows = int(input("Enter number of rows: "))
    if rows < 1 or rows > 20:
        raise ValueError
except ValueError:
    print("\nInvalid number of rows.")
    sys.exit()
print()
image = draw_triangle_segment(height)
draw(image, height, rows)
