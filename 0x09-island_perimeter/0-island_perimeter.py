#!/usr/bin/python3
"""island perimeter"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    count = 0
    for column in range(len(grid)):
        for row in range(len(grid[column])):
            if grid[column][row] == 1:
                if column - 1 < 0:
                    count += 1
                else:
                    try:
                        if grid[column - 1][row] == 0 or column - 1 < 0:
                            count += 1
                    except:
                        pass
                if column + 1 > len(grid) - 1:
                    count += 1
                else:
                    try:
                        if grid[column + 1][row] == 0:
                            count += 1
                    except:
                        pass
                if row + 1 > len(grid[column]) - 1:
                    count += 1
                else:
                    try:
                        if grid[column][row + 1] == 0:
                            count += 1
                    except:
                        pass
                try:
                    if grid[column][row - 1] == 0 or row - 1 < 0:
                        count += 1
                except:
                    pass
    return count
