#!/usr/bin/python3
"""making_change"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to
    meet a given amount total
    """
    if total < 1:
        return 0
    num_coins = len(coins)
    max_value = total + sum(coins)

    change = [[max_value] * (total + 1) for _ in range(num_coins + 1)]
    for i in range(num_coins + 1):
        change[i][0] = 0
    for i in range(1, num_coins + 1):
        coin_value = coins[i - 1]
        for j in range(1, total + 1):
            if coin_value > j:
                change[i][j] = change[i - 1][j]
            else:
                change[i][j] = min(change[i - 1][j], 1 + change[i][j - coin_value])
    
    if change[num_coins][total] != max_value:
        return change[num_coins][total]
    else:
        return -1
