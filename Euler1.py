import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip()) - 1
    sum = 0
    num3 = n // 3
    num5 = n // 5
    num15 = n // 15
    sum3 = 3*num3 * (num3 + 1) // 2
    sum5 = 5*num5 * (num5 + 1) // 2
    sum15 = 15*num15 * (num15 + 1) // 2
    sum = sum3 + sum5 - sum15
    print(sum)
