#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """
    Returns a list of primes up to n using the sieve of Eratosthenes.

    Args:
        n (int): The upper limit of the range to find primes.

    Returns:
        list: A list of prime numbers up to n.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def play_game(n):
    """
    Simulates a single game of prime number removal and returns the winner.

    Args:
        n (int): The upper limit of the set of integers.

    Returns:
        str: The winner of the game ("Maria" or "Ben").
    """
    primes = sieve_of_eratosthenes(n)
    numbers = [True] * (n + 1)  # True means the number is available
    turn = 0  # 0 for Maria, 1 for Ben

    while primes:
        prime = primes.pop(0)  # Pick the smallest prime available
        if numbers[prime]:
            for i in range(prime, n + 1, prime):
                numbers[i] = False
            turn = 1 - turn

    return "Maria" if turn == 1 else "Ben"


def is_winner(x, nums):
    """
    Determines the winner of x rounds of the prime game.

    Args:
        x (int): The number of rounds to play.
        nums (list): A list of integers representing the upper limits for each round.

    Returns:
        str: The player who won the most rounds ("Maria" or "Ben").
        None: If there is a tie.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

