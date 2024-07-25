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
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Loop through each integer in the data list
    for num in data:
        # Get the 8 least significant bits of the integer
        byte = num & 0xFF

        # If this is the start of a new UTF-8 character
        if n_bytes == 0:
            # Count the number of leading 1s in the byte
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask >>= 1

            # 1-byte character
            if n_bytes == 0:
                continue

            # Invalid scenarios according to UTF-8
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if the byte is of the form 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes left in the current UTF-8 character
        n_bytes -= 1

    # If there are leftover bytes, the data is invalid
    return n_bytes == 0


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
