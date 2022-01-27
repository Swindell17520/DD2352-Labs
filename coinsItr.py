# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 14:34:57 2022

@author: Rahul
"""
n = int(input())
a = int(input())
b = int(input())
c = int(input())

coins = [a, b, c]


def Coins(n):
    dp = [float('inf')] * (n + 1)  # initialize result array with default value inf
    dp[0] = 0  # base case
    for amount in range(1, n + 1):
        for coin in coins:
            if amount - coin >= 0:
                # checking if this path is shorter than the other computed before
                dp[amount] = min(dp[amount], dp[amount-coin] + 1)
        if dp[amount] == float('inf'):
            # if no silver/gold/platinum were found...
            dp[amount] = amount
    result = dp[-1]
    return result if result != float('inf') else 0


print(Coins(n))
