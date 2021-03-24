import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    pallindrome = 0
    for i in range(100, 1000):      
        num = i * i if i * i > pallindrome else ((pallindrome // i) + 1) * i
        limit = n if i * 1000 > n else i * 1000
        while num < limit:            
            if str(num)[:3] == str(num)[:-4:-1] and num > pallindrome:
                pallindrome = num
            num += i
    print(pallindrome)

    
