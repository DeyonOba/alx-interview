#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n, they take turns choosing a prime
number from the set and removing that number and its multiples from the
set. The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.

    - Prototype: def isWinner(x, nums)
    - where x is the number of rounds and nums is an array of n
    - Return: name of the player that won the most rounds
    - If the winner cannot be determined, return None
    - You can assume n and x will not be larger than 10000
    - You cannot import any packages in this task
Example:

    - x = 3, nums = [4, 5, 1]

First round: 4
    - Maria picks 2 and removes 2, 4, leaving 1, 3
    - Ben picks 3 and removes 3, leaving 1
    - Ben wins because there are no prime numbers left for Maria to
    choose

Second round: 5
    - Maria picks 2 and removes 2, 4, leaving 1, 3, 5
    - Ben picks 3 and removes 3, leaving 1, 5
    - Maria picks 5 and removes 5, leaving 1
    - Maria wins because there are no prime numbers left for Ben to
    choose

Third round: 1
    - Ben wins because there are no prime numbers for Maria to choose

Result: Ben has the most wins
"""


def find_prime_numbers(n):
    """Finds prime numbers within a specified range."""
    if n < 1:
        return
    prime_numbers = []
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


def isWinner(x, nums):
    """
    Finds the winner between Maria and Ben in a prime game.

    Args:
        x(int): Number of rounds
        nums(list): Array of n

    Returns:
        str: Maria or Ben
        None: if no winner is found
    """
    # Checks if the number of round is less than 1
    if x < 1:
        return

    track_players_scores = dict([('Maria', 0), ('Ben', 0)])

    # Iterate through the rounds and the number picked at each round
    for round, n in enumerate(nums):
        # Uncomment the interactive debugger below
        # print(f"Round {round + 1}: {n}")
        # If number picked is less than 1 skip round
        if n < 1:
            continue
        # If number picked is 1 than no prime number is found
        # Ben wins the round
        if n == 1:
            track_players_scores['Ben'] += 1
            # Uncomment the interactive debugger below
            # print('\t\tBen wins this round')
            continue
        # Player Maria always goes first, variable `marias_turn`
        # controls who plays at each round
        marias_turn = True
        # Get the prime numbers for the current rounds number
        prime_numbers = find_prime_numbers(n)

        # Uncomment the interactive debugger below
        # print(f"\tPrime Numbers found: {prime_numbers=}")
        # Get the available number that could be picked by Maria,
        # and Ben
        number_pool = list(range(2, n + 1))
        # Uncomment the interactive debugger below
        # print(f"\t{number_pool=}")
        # Iterate through the prime number found
        for prime_number in prime_numbers:
            # Uncomment the interactive debugger below
            # print(
            # f"\tIt's {'Marias' if marias_turn else 'Bens'}\
            # turn to play."
            # )
            # print("\t\tPrime number picked is", prime_number)

            # Filter out the factors of the current prime number
            number_pool = list(filter(
                lambda x: x % prime_number != 0,
                number_pool
                ))
            # Uncomment the interactive debugger below
            # print(f"\t\t{number_pool=}")

            # Condition checks if the number pool is empty
            if not number_pool:
                # If number pool is emptied on Marias turn
                # then Maria wins, else Ben wins
                if marias_turn:
                    # print("\t\tMaria wins this round\n")
                    track_players_scores['Maria'] += 1
                else:
                    # print("\t\tBen wins this round\n")
                    track_players_scores['Ben'] += 1
                # Winner of the round has been found, end the round
                break
            # Update who is to play next
            if marias_turn:
                marias_turn = False
            else:
                marias_turn = True
    # Final result of the game
    if track_players_scores['Maria'] == track_players_scores['Ben']:
        return
    elif track_players_scores['Maria'] > track_players_scores['Ben']:
        return "Maria"
    else:
        return "Ben"
