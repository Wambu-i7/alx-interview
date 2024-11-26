#!/usr/bin/python3
"""Make Change"""

def makeChange(coins, total):
    """
    This function determines the fewest number of coins
    needed to make a given total.
    If the total is 0 or less, it returns 0.
    If it's not possible to make the total
    using the provided coins, it returns -1.
    The function uses a dynamic programming
    approach to find the minimum number of coins required.

    coins: list of integers representing the
    available coin denominations.
    total: integer representing the amount to be made using the coins.
    """
    if total <= 0:
        return 0
    
    dp = [total + 1] * (total + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[total] if dp[total] <= total else -1
