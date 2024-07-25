#!/usr/bin/python3
"""
Write a method that determines if a given data set represents a
valid UTF-8 encoding.

    - Prototype: def validUTF8(data)
    - Return: True if data is a valid UTF-8 encoding, else return False
    - A character in UTF-8 can be 1 to 4 bytes long
    - The data set can contain multiple characters
    - The data will be represented by a list of integers
    - Each integer represents 1 byte of data,
    therefore you only need to handle the 8 least significant bits of
    each integer
"""
from typing import List


def verify_int_range(num):
    """Verifies integer number and ASCII range."""
    if type(num) is int and 0 <= num < 255:
        return True
    return False


def validUTF8(data: List[int]) -> bool:
    """Checks for valid UTF-8 characters"""
    if type(data) is not list:
        return False
    return all([verify_int_range(num) for num in data])


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [
        80, 121, 116, 104, 111, 110,
        32, 105, 115, 32, 99, 111, 111, 108, 33
        ]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
