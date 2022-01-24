# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 14:06:48 2022

@author: Rahul
"""
import sys
sys.setrecursionlimit(100000)
n = 10
a = 5
b =6
c = 7
def Coins(n):
    if n == 0:
        return 0
    elif n < 0:
        return float('inf')
    else:
        return min(n,1+Coins(n-a),1+Coins(n-b),1+Coins(n-c))
    
    