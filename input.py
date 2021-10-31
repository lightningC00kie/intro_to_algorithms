import random
l = []
for i in range(1000):
    l.append(str(random.randint(1,1_000_001)))


print(' '.join(l))