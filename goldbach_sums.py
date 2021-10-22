n = input()
l = [int(i) for i in n.split()]
count = [0] * len(l)
largest = max(l)



for i in range(len(l)):
    if l[i] % 2 != 0 and l[i] > 3:
        a = 2
        b = l[i] - 2
    else:
        for ii in range(2, (l[i]//2)+1):

            a = ii
            b = l[i] - ii

    prime = [True] * (b+1)
    j = 2

    while j * j <= b:
        if prime[j]:
            for m in range(j*2, b+1, j):
                prime[m] = False
        j += 1

    if prime[a] and prime[b]:
        count[i] += 1
        
c = [str(i) for i in count]

c = ' '.join(c)
print(c)