# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 14:34:57 2022

@author: Rahul
"""
import sys
n = int(input())
a = int(input())
b = int(input())
c = int(input())
def min(x, y):
  if x < y:
    return x
  return y

def coin_change(f, n, k):
  M = [0]*(n+1)

  for j in range(1, n+1):
    mini = float('inf')

    for i in range(1, k+1):
      if(j >= f[i]):
        mini = min(mini, 1+M[j-f[i]])
    M[j] = mini
  return M[n]

f = [0,a,b,c]
print(coin_change(f, n, 3))
