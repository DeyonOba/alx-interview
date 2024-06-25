#!/usr/bin/python3
"""
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Create a function def pascal_triangle(n):
    that returns a list of lists of integers representing
    the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
You are not allowed to import any module
"""


def pascal_triangle(n: int) -> list:
    """Creates a Pascal's Triangle."""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    array = [[1], [1, 1]]

    if n == 2:
        return array

    for idx in range(1, n - 1):
        last_array = array[idx]
        new_array = []

        for jdx in range(idx + 2):
            if jdx == 0:
                new_array.append(1)
            elif jdx < idx + 1:
                new_array.append(last_array[jdx-1] + last_array[jdx])

        new_array.append(1)
        array.append(new_array)

    return array


if __name__ == "__main__":
    triangle = pascal_triangle(5)

    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
