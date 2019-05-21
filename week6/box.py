import sys

if len(sys.argv) == 1:
    print("No arguments")
    sys.exit()
elif len(sys.argv) < 3:
    print("Too few arguments")
    sys.exit()
elif len(sys.argv) > 3:
    print("Too many arguments")
    sys.exit()
else:
    try:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
    except ValueError:
        print("Invalid arguments")
        sys.exit()

if width < 0 and height < 0:
    print("Negative dimensions")
    sys.exit()
elif height < 0:
    print("Negative height")
    sys.exit()
elif width < 0:
    print("Negative width")
    sys.exit()

for row in range(height):
    print(width*"*")
