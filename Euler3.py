import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    m = n
    winner = 1
    for i in range(math.floor(math.sqrt(n))):
        while m % (i + 2) == 0:
            m //= i + 2
            winner = i + 2
        if m == 1:
            break
    if m != 1:
        winner = m
    
    print(winner)
