import sys

inp = []
count = 0

for line in sys.stdin:
    inp.append(line.strip().split())
    count += 1
    if count == 3:
        break

n = int(inp[0][0])
a = [int(i) for i in inp[1]]
f = [int(i) for i in inp[2]]

def binary_search(a, f, lookLeft, lookRight):
    lo = 0
    hi = len(a) - 1
    start_ind = -1
    end_ind = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] < f:
            lo = mid + 1
        elif a[mid] > f:
            hi = mid - 1
        elif a[mid] == f:
            if lookLeft:
                start_ind = mid
                hi = mid - 1
            elif lookRight:
                end_ind = mid
                lo = mid + 1
            else:
                return mid
    return [start_ind, end_ind]

def find_occurunces(n, a, f):
    
    res = [0] * len(f)
    start = []
    end = []
    for i in range(len(f)):
        if binary_search(a, f[i], False, False) == None:
            start.append(-1)
            end.append(-1)
            continue

        start_ind = binary_search(a, f[i], True, False)[0]
        start.append(start_ind)
        end_ind = binary_search(a, f[i], False, True)[1]
        end.append(end_ind)

    for i in range(len(start)):
        if start[i] != -1 and end[i] != -1:
            res[i] += (end[i] - start[i]) + 1
        print(res[i])
    
find_occurunces(n, a, f)