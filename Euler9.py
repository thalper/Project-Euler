import sys

t = int(input().strip())
triplets = {}
for m in range(1,32):
    n = m + 1
    while m*m + n*n < 1500:
        a = n*n - m*m
        b = 2*m*n
        c = m*m + n*n
        if a+b+c < 3001 and (a+b+c not in triplets or a*b*c > triplets[a+b+c]):
            triplets.update({a+b+c: a*b*c})
        multiple = 2
        while (a+b+c)*multiple < 3001:
            if (multiple*a+multiple*b+multiple*c not in triplets or multiple*multiple*multiple*a*b*c > triplets[multiple*a+multiple*b+multiple*c]):
                triplets.update({multiple*a+multiple*b+multiple*c: multiple*multiple*multiple*a*b*c})
            multiple += 1
        n += 1

    
for a0 in range(t):
    n = int(input().strip())
    if n in triplets:
        print(triplets[n])
    else:
        print("-1")
    