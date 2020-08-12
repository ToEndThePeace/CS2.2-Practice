# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
from graph1 import Graph


# this has 4 islands
islands1 = [[0, 1, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 0, 0]]

islands2 = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
            [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]


def island_counter(matrix):
    count = 0
    # keep track of visited nodes
    # visited = set()
    visited = []
    for _ in range(len(matrix)):
        new_row = [False] * len(matrix[0])
        visited.append(new_row)

    """
    walk through every cell in the grid
    if it hasn't been visited and it's a 1,
        do a traversal
        add all traversed nodes to visited
        increment the counter
    """
    def get_neighbors(x, y):
        """
        get neighbors checks a coordinate in the grid
        and returns a list of neighboring indices that
        have the value of 1
        """
        neighbors = []

        if x > 0 and matrix[x - 1][y] == 1:
            neighbors.append((x - 1, y))
        if y > 0 and matrix[x][y - 1] == 1:
            neighbors.append((x, y - 1))
        if x < len(matrix) - 1 and matrix[x + 1][y] == 1:
            neighbors.append((x + 1, y))
        if y < len(matrix[0]) - 1 and matrix[x][y + 1] == 1:
            neighbors.append((x, y + 1))

        return neighbors

    def dft(row, col):
        """
        dft (depth-first-traversal) flags all connected
        nodes of a given node as visited, that's all
        """
        s = [(row, col)]
        while len(s) > 0:
            x, y = s.pop()
            if not visited[x][y]:
                visited[x][y] = True
                for n in get_neighbors(x, y):
                    s.append(n)

    # this loop goes over every matrix node and counts islands
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not visited[i][j]:
                if matrix[i][j] == 1:
                    dft(i, j)
                    count += 1
    return count


print(island_counter(islands2))
