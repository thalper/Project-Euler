import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    largest = 0
    for x in range(n-k):
        current = 1
        for y in range(k):
            current *= int(num[x+y])
        if current > largest:
            largest = current
    print(largest)
