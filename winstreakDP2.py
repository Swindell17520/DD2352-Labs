import sys
import timeit
import math
sys.setrecursionlimit(10000000)
n = 8000
k = round(n/2,0)
p = 0.99
dp = {}
start = timeit.default_timer()
def Win_Streak(x):
    if x in dp:
        return dp[x]
    elif x < k:
        return 0.0
    elif x == k:
        return math.pow(p,k)
    else:
        dp[x] = Win_Streak(x-1) + math.pow(p,k)*(1 - Win_Streak(x-k-1))*(1-p)
        return dp[x]


Win_Streak(n)
stop = timeit.default_timer()
execution_time = stop - start
print("Program Executed in "+str(execution_time))
