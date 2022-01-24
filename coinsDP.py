# Coin problem with top-down implementation

import sys

sys.setrecursionlimit(100000)
n = int(input())
a = int(input())
b = int(input())
c = int(input())

dp = {}

def Coins(n):
    if n in dp:
        return dp[n]
    elif n < 0:
        return float('inf')
    elif n == 0:
        return 0
    else:
        dp[n] = min(n, 1 + Coins(n - a), 1 + Coins(n - b), 1 + Coins(n - c))
        return dp[n]


print(Coins(n))
