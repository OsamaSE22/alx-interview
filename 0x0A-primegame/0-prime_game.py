#!/usr/bin/python3

def is_winner(x, nums):
    maria_wins, ben_wins = 0, 0

    for _ in range(x):
        remaining_nums = nums.copy()
        current_player = "Maria"  # Maria starts first

        while remaining_nums:
            prime = find_first_prime(remaining_nums)
            if prime is None:
                if current_player == "Maria":
                    ben_wins += 1
                else:
                    maria_wins += 1
                break
            remove_multiples(remaining_nums, prime)
            current_player = "Ben" if current_player == "Maria" else "Maria"

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return "None"

def find_first_prime(nums):
    for num in nums:
        if is_prime(num):
            return num
    return None

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def remove_multiples(nums, prime):
    i = 0
    while i < len(nums):
        if nums[i] % prime == 0:
            del nums[i]
        else:
            i += 1

# Example usage
x = 5
nums = [2, 5, 1, 4, 3]
winner = isWinner(x, nums)
print("Winner:", winner)

