import sys

def nextPrime(j, primeList):
    notPrime = True
    while notPrime:
        j += 1
        notPrime = False
        for x in primeList:
            if j % x == 0:
                notPrime = True
                break
    return j
        
        
t = int(input().strip())
primeList = []
for a0 in range(t):
    n = int(input().strip())
    for i in range(n-len(primeList)):
        if primeList == []:
            j = 1
        j = nextPrime(j, primeList)
        primeList.append(j)
    print(primeList[n-1])
    