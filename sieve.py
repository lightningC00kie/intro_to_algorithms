n = int(input())
prime = [True] * n

i = 2
while i * i <= n:
    if prime[i]:
        for ii in range(i*2, n, i):
            prime[ii] = False
    i += 1

for i in range(1000, 0, -1):
    if prime[i]:
        print(i)
        break