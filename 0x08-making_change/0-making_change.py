#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest
number of coins needed to meet a given amount total.

    - Prototype: def makeChange(coins, total)
    - Return: fewest number of coins needed to meet total
        - If total is 0 or less, return 0
        - If total cannot be met by any number of coins you have,
        return -1
    - coins is a list of the values of the coins in your possession
    - The value of a coin will always be an integer greater than 0
    - You can assume you have an infinite number of each denomination
    of coin in the list
    - Your solution’s runtime will be evaluated in this task
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Determines the fewest number of coins needed to meet a given amount
    total.

    Args:
        coins(List[int]): List of available change denomination.
        total(int): Total amount given to make change from.

    Returns:
        int:
            - A positive integer if combination is found.
            - 0 if total is 0.
            - -1 if total cannot be met by any number of coins.
    """
    # If total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    # Initialize the dp array with inf (an amount we cannot achieve)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make amount 0

    # Iterate through each coin and update the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still inf, it means the amount cannot be met
    return dp[total] if dp[total] != float('inf') else -1
