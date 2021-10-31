n = input().split()
l = [int(i) for i in n]
count = [0] * len(l)
largest = max(l)

prime = [True] * (largest+1)
j = 2

while j * j <= largest:
    if prime[j]:
        for m in range(j*2, largest+1, j):
            prime[m] = False
    j += 1

for i in range(len(l)):
    if l[i] == 4:
        count[i] += 1
    if l[i] % 2 != 0 and l[i] > 3:
        a = 2
        b = l[i] - 2
        if prime[b]:
            count[i] += 1
            continue
    else:
        for ii in range(3, (l[i]//2)+1, 2):

            a = ii
            b = l[i] - ii
            if prime[a] and prime[b]:
                count[i] += 1

c = [str(i) for i in count]

c = ' '.join(c)
print(c)

        