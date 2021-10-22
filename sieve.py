n = int(input())
prime = [True] * n

i = 2
while i * i <= n:
    if prime[i]:
        for ii in range(i*2, n, i):
            prime[ii] = False
    i += 1
