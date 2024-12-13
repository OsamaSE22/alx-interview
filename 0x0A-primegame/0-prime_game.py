#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of 'x' rounds of the Prime Game, given a list 'nums'.

    Args:
        x: Number of rounds (integer, 1 to 10000).
        nums: List of consecutive integers (1 to n, n <= 10000).

    Returns:
        String: Name of the winner ("Maria", "Ben"), or "None" if winner cannot be determined.
    """

    # Initialize wins for both players
    maria_wins, ben_wins = 0, 0

    for _ in range(x):  # Loop for each round
        # Create a copy to avoid modifying original list
        remaining_nums = nums.copy()

        # Maria's turn (always starts)
        while True:
            # Find the first prime number in the remaining list
            prime = find_first_prime(remaining_nums)
            if prime is None:
                break  # No prime found, Ben wins the round
            # Remove the prime and its multiples
            remove_multiples(remaining_nums, prime)

        # Ben's turn (if Maria didn't lose)
        while True:
            prime = find_first_prime(remaining_nums)
            if prime is None:
                maria_wins += 1  # Ben couldn't move, Maria wins the round
                break
            remove_multiples(remaining_nums, prime)

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return "None"  # Tie (equal wins)

def find_first_prime(nums):
    """
    Finds the first prime number in the given list 'nums'.

    Args:
        nums: List of integers.

    Returns:
        Integer: The first prime number found, or None if no prime is found.
    """

    for num in nums:
        if is_prime(num):
            return num
    return None

def is_prime(num):
    """
    Checks if a number 'num' is prime.

    Args:
        num: Integer.

    Returns:
        Boolean: True if 'num' is prime, False otherwise.
    """

    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def remove_multiples(nums, prime):
    """
    Removes the prime number 'prime' and its multiples from the list 'nums'.

    Args:
        nums: List of integers (modified in-place).
        prime: Integer, the prime number to remove.
    """

    """
    This function iterates through the list 'nums' and removes all occurrences
    of the prime number 'prime' and its multiples. It modifies the list 'nums'
    in-place.
    """

    i = 0
    while i < len(nums):
        if nums[i] % prime == 0:
            del nums[i]  # Remove the element at index i
        else:
            i += 1  # Move to the next element only if not a multiple
