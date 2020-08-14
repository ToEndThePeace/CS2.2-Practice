"""

"""

image = [list("...#######........"),
         list("...#.....#........"),
         list("...#.....#........"),
         list("...#..######......"),
         list("...#..#....#......"),
         list("...####....######."),
         list("....#...........#."),
         list("....###.#########."),
         list("......#.#.........")]


def print_image():
    for line in image:
        print("".join(line))
    print("\n")


def floodfill(row, col, c):
    if row < 0 or row > len(image) - 1 or col < 0 or col > len(image[0]) - 1:
        return
    if image[row][col] != '.':
        return
    image[row][col] = c
    # print_image()
    floodfill(row - 1, col, c)
    floodfill(row + 1, col, c)
    floodfill(row, col - 1, c)
    floodfill(row, col + 1, c)

def fillstroke(row, col, c):
    if row < 0 or row > len(image) - 1 or col < 0 or col > len(image[0]) - 1:
        return
    if image[row][col] != "#":
        return
    image[row][col] = c
    fillstroke(row - 1, col, c)
    fillstroke(row + 1, col, c)
    fillstroke(row, col - 1, c)
    fillstroke(row, col + 1, c)

print_image()
floodfill(2, 5, '?')
print_image()
floodfill(5, 9, '*')
print_image()
floodfill(0, 0, '0')
print_image()
fillstroke(0, 4, "x")
print_image()