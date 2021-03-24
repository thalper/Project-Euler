import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n < 2:
        print("0")
    sum = 0
    prev1 = 1
    prev2 = 2
    temp = 2
    while temp < n:
        if temp % 2 == 0:
            sum += temp
        temp = prev1 + prev2
        prev1 = prev2
        prev2 = temp
    print(sum)
