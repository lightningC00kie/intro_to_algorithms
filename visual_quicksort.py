import sys

inp = []
for lines in sys.stdin:
    inp += lines.split()
    break

inp = [int(i) for i in inp]

def partition(a, lo, hi, level):
    
    pivot = a[hi-1]
    k = lo
    for i in range(lo, hi):
        if a[i] <= pivot: 
            a[k], a[i] = a[i], a[k]
            k += 1
    k -= 1
    if k == 0:
        print(f'{level+1:02d}:', end='')
    else: 
        print(f'{level+1:02d}:', end=' ')

    for i in range(len(a)):
        if i not in range(lo, hi):
            if i+1 == k:
               print(f' '*2, end='')
            else:
               print(f' '*3, end='')
        else:
            if i == 0 and i==k:
                print(f'[{a[i]:02d}', end = ']')
            elif i == k:
                print(f'[{a[i]:02d}', end = ']')
            else:
                if i+1 == k:
                    print(f'{a[i]:02d}', end='')
                else:
                    print(f'{a[i]:02d}', end=' ')
    print('')
    return k

def quickSort(a, lo, hi, level=0):
    if hi - lo <= 1:
        return

    k = partition(a, lo, hi, level)
    
    quickSort(a, lo, k,level=level+1)
    quickSort(a, k+1, hi,level=level+1)

def quick(a):
    print('00:', end= ' ')
    for i in a:
        print(f'{i:02d}', end=' ')
    print(' ')
    quickSort(a, 0, len(a))
    print('00:', end = ' ')
    for i in a:
        print(f'{i:02d}', end=' ')
    print(' ')
    return

quick(inp)