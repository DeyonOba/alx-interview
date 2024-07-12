#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n,
write a method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste =>
HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
"""


def find_prime_numbers(n):
    """Finds prime numbers within a specified range."""
    if n < 1:
        return
    prime_numbers = [1]
    if n == 1:
        return prime_numbers

    for number in range(2, n + 1):
        is_prime = True
        for prime_number in prime_numbers:
            if prime_number != 1 and number % prime_number == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(number)
    return prime_numbers


def minOperations(n):
    """
    Finds the minimum number of operation needed to reach the target.
    """
    if n < 1:
        return 0
    if n == 1:
        return n
    num_of_operations = 0
    num_char_stored = 1
    prev_num_char_stored = 1
    mid = n // 2 if n % 2 != 0 else n / 2
    is_even = True if n % 2 == 0 else False

    def copy_and_paste():
        """Implements the operation copy and paste."""
        nonlocal num_char_stored, num_of_operations, prev_num_char_stored
        prev_num_char_stored = num_char_stored
        num_char_stored *= 2
        num_of_operations += 2

    def paste():
        """Implements the operation paste."""
        nonlocal num_char_stored, num_of_operations
        num_char_stored += prev_num_char_stored
        num_of_operations += 1

    while num_char_stored < n:
        if n % num_char_stored == 0:
            copy_and_paste()
        else:
            paste()
    if num_char_stored == n:
        return num_of_operations
    return 0
