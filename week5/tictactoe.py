import sys

circ = "O"
cross = "X"
empty = " "
grid = ([empty, empty, empty], [empty, empty, empty], [empty, empty, empty])
turn = 0


def draw_Grid(grid):
    print("{}|{}|{}".format(grid[0][0], grid[0][1], grid[0][2]))
    print(5*"-")
    print("{}|{}|{}".format(grid[1][0], grid[1][1], grid[1][2]))
    print(5*"-")
    print("{}|{}|{}".format(grid[2][0], grid[2][1], grid[2][2]))


def place_tictac(grid, player, x, y):
    if grid[y][x] == empty:
        grid[y][x] = player


def check_game_state(grid, x, y):
    # check vertically
    global turn
    empty = " "
    game_state = True
    check_empty1 = grid[0][0] != empty
    check_empty2 = grid[0][2] != empty
    if grid[y][0] == grid[y][1] and grid[y][1] == grid[y][2]:
        game_state = False
    if grid[0][x] == grid[1][x] and grid[1][x] == grid[2][x]:
        game_state = False
    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and check_empty1:
        game_state = False
    if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and check_empty2:
        game_state = False
    return game_state


def ask_coordinates():
    coord = input()
    coord = coord.split(" ")
    x = int(coord[0])
    y = int(coord[1])
    return (x, y)


while True:
    # player one's turn, in form (column, row)
    x, y = ask_coordinates()
    place_tictac(grid, cross, x, y)
    flag = check_game_state(grid, x, y)
    if not check_game_state(grid, x, y):
        print("{} wins!\n".format(cross))
        draw_Grid(grid)
        print()
        break
    turn += 1
    if turn == 9:
        print("Draw\n")
        draw_Grid(grid)
        print()
        break
    print()
    draw_Grid(grid)
    print()
    x, y = ask_coordinates()
    place_tictac(grid, circ, x, y)
    flag = check_game_state(grid, x, y)
    if not check_game_state(grid, x, y):
        print("{} wins!\n".format(circ))
        draw_Grid(grid)
        print()
        break
    turn += 1
    if turn == 9:
        print("Draw\n")
        draw_Grid(grid)
        print()
        break
    print()
    draw_Grid(grid)
    print()
