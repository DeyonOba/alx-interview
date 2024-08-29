#!/usr/bin/python3
"""
Island Perimeter

Create a function def island_perimeter(grid): that returns the
perimeter of the island described in grid:

    - grid is a list of list of integers:
        - 0 represents water
        - 1 represents land
        - Each cell is square, with a side length of 1
        - Cells are connected horizontally/vertically (not diagonally).
        - grid is rectangular, with its width and height not exceeding 100
    - The grid is completely surrounded by water
    - There is only one island (or nothing).
    - The island doesn’t have “lakes” (water inside that isn’t
    connected to the water surrounding the island).
"""
from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """
    Calculate the perimeter of an island grid.

    Args:
        grid (List[List[int]]): A grid contain island land mass

    Returns:
        int: Perimeter of island
    """
    perimeter = 0
    row = len(grid)
    column = len(grid[0])
    for i in range(row):
        for j in range(column):
            if grid[i][j] == 1:
                if (i - 1) >= 0:
                    if grid[i-1][j] == 0:
                        perimeter += 1
                if (i + 1) < row:
                    if grid[i+1][j] == 0:
                        perimeter += 1
                if (j - 1) >= 0:
                    if grid[i][j-1] == 0:
                        perimeter += 1
                if (j + 1) < column:
                    if grid[i][j+1] == 0:
                        perimeter += 1
    return perimeter
