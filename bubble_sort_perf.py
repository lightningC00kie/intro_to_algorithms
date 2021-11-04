import time
import random

def bubble_sort(): 
    n = [i * 1000 for i in range(1,101)]
    for i in n:
        tmp = i
        l = [random.randint(1, j+1) for j in range(i)]
        tic = time.perf_counter()
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
        toc = time.perf_counter()
        print(tmp, toc-tic)

bubble_sort()