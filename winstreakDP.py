import sys
import timeit
sys.setrecursionlimit(100000)
n = int(input())
k = int(input())
p = float(input())
dp = {}
start = timeit.default_timer()
def Win_Streak(n,k):
    if n and k in dp:
        return dp[n][k]
    elif k == 0:
        return 1.0
    elif n == 0 and k > 0:
        return 0.0
    else:
        dp[n][k] = p*Win_Streak(n-1,k-1) + (1-p)*Win_Streak(n-1,k)
        return dp[n]


print(Win_Streak(n,k))
stop = timeit.default_timer()
execution_time = stop - start
print("Program Executed in "+str(execution_time))
