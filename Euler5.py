import sys
import math

def prime(i):
    if i == 2:
        return True
    for j in range(2, math.ceil(math.sqrt(i)) + 1):
        if i % j == 0:
            return False
    return True

    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    primes = []
    for i in range(2,n+1):
        if prime(i):
            j = i
            while j <= n:
                primes.append(i)
                j *= i 
    product = 1
    for x in primes:
        product *= x    
    print(product)

