#!/usr/bin/python3
def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """Returns a list of primes up to n using the sieve of Eratosthenes"""
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(2, n + 1) if sieve[i]]

    def play_game(n):
        """Simulates a single game and returns the winner (Maria or Ben)"""
        primes = sieve_of_eratosthenes(n)
        numbers = [True] * (n + 1)  # True means the number is still available
        turn = 0  # 0 for Maria, 1 for Ben
        
        while primes:
            prime = primes.pop(0)  # Pick the smallest prime available
            if numbers[prime]:
                # Mark all multiples of the prime as removed
                for i in range(prime, n + 1, prime):
                    numbers[i] = False
                # Alternate turn
                turn = 1 - turn
            else:
                break
        
        # If turn is 1, it means it was Ben's turn last, so Maria wins
        return "Maria" if turn == 1 else "Ben"
    
    # Count wins for each player
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1
    
    # Return the name of the player who won the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

