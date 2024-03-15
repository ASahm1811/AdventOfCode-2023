from main import lines

found_steps = []


def fillGrid(grid):
    for line in lines:
        lst = []
        for char in line:
            lst.append(char)
        grid.append(lst)

    return grid


def executeHike(grid, i, j, steps):
    if i == 0:
        grid[i][j] = 'S'
    else:
        grid[i][j] = 'O'

    if 0 < j < len(grid[i]):
        if i == 0:
            if grid[i][j - 1] == '.' or grid[i][j - 1] == '<':
                executeHike(grid, i, j - 1, steps + 1)
            if grid[i][j + 1] == '.' or grid[i][j + 1] == '>':
                executeHike(grid, i, j + 1, steps + 1)
            if grid[i + 1][j] == '.' or grid[i + 1][j] == 'v':
                executeHike(grid, i + 1, j, steps + 1)
        if 0 < i < len(grid) - 1:
            if grid[i][j - 1] == '.' or grid[i][j - 1] == '<':
                executeHike(grid, i, j - 1, steps + 1)
            if grid[i][j + 1] == '.' or grid[i][j + 1] == '>':
                executeHike(grid, i, j + 1, steps + 1)
            if grid[i + 1][j] == '.' or grid[i + 1][j] == 'v':
                executeHike(grid, i + 1, j, steps + 1)
            if grid[i - 1][j] == '.' or grid[i - 1][j] == '^':
                executeHike(grid, i - 1, j, steps + 1)
    found_steps.append(steps)
    return max(found_steps)


def calc():
    grid = fillGrid([])
    no_steps = executeHike(grid, 0, 1, 0)

    return no_steps


# print(calc())
