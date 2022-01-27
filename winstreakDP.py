import sys
import timeit
sys.setrecursionlimit(10000000)
n = 4800
k = round(n/2,0)
p = 0.99
y = k
dp = {}
start = timeit.default_timer()
def Win_Streak(x,y):
    if (x,y) in dp:
        return dp[(x,y)]
    elif y == 0:
        return 1.0
    elif x == 0 and y > 0:
        return 0.0
    else:
        dp[(x,y)] = p*Win_Streak(x-1,y-1) + (1-p)*Win_Streak(x-1,k)
        return dp[(x,y)]


Win_Streak(n,k)
stop = timeit.default_timer()
execution_time = stop - start
print("Program Executed in "+str(execution_time))
