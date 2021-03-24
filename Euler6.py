import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sumN = int((n+1)*(n/2))
    sumNsquared = sumN * sumN
    sumSquaredN = 0
    for i in range(1,n+1):
        sumSquaredN += i*i
    print(sumNsquared - sumSquaredN)
