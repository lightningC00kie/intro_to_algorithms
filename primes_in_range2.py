import math
n = int(input())

prime = [True] * (n+1)
prime[0] = prime[1] = False

for i in range(2, round(math.sqrt(n))):
    if prime[i]:
        for j in range(i*2, n+1, i):
            prime[j] = False

for i in range(len(prime)):
    if prime[i]:
        print(i)