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


def island_perimeter(grid) -> int:
    """
    Calculate the perimeter of an island grid.

    Args:
        grid (List[List[int]]): A grid contain island land mass

    Returns:
        int: Perimeter of island
    """
    perimeter = 0
    # Get the number of rows and columns in the grid
    n_rows = len(grid)
    n_columns = len(grid[0])

    # Iterate through each row and column in the grid
    for r in range(n_rows):
        for c in range(n_columns):
            # Checks for land mass (i.e 1)
            if grid[r][c] == 1:
                # Check if the current row is the first row
                # (i.e row idx 0)
                # There would be no water at the edge of the grid,
                # increment the perimeter value by 1
                # or Check if the row above has a water mass then
                # increment the perimeter value by 1
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1
                # Check if the current row is at the end of the grid
                # increment the perimeter by 1
                # or Check if the next row below has a water mass
                # (i.e 0) increment the perimeter by 1
                if r == n_rows - 1 or grid[r+1][c] == 0:
                    perimeter += 1
                # Check if the current column is the first column
                # increment the perimeter by 1
                # or Check if the left column has a water mass then
                # increment the perimeter by 1
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1
                # Check if the current column is at the end of the grid
                # increment the perimeter by 1
                # or Check if the neighbouring column on the right has
                # a water mass, then increment perimeter by 1.
                if c == n_columns - 1 or grid[r][c+1] == 0:
                    perimeter += 1
    return perimeter
