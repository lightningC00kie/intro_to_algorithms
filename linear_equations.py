import sys
inp = []
for line in sys.stdin:
    inp.append(line.split())
    inp = [[int(inp[i][j]) for j in range(len(inp[i]))] for i in range(len(inp))]

n = inp.pop(0)[0]

def find_pivot(a, r):
    for i in range(len(a[r])):
        if a[r+1][i] != 0:
            return a[r][i], i
        # if a[r][i] != 0 and a[r+1][i] != 0:
        #     return a[r][i], i
        return None, None

def leading_zeroes(a):
    zeroes = [0] * len(a)

    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 0:
                zeroes[i] += 1
            else:
                break
    return zeroes

def rearrange_rows(a):
    zeroes = leading_zeroes(a)
    for i in range(len(a)-1):
        if zeroes[i] > zeroes[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    return a

def eliminate(a, m, row):
    for i in range(n):
        a[row][i] -= a[row-1][i] * m
    return a
        

def ref(a):
    for i in range(len(a)):
        a = rearrange_rows(a)
        if i + 1 <= n:
            pivot, index = find_pivot(a, i)
        else:
            break
        if pivot == None:
            break
        multi_by = a[i+1][index]/pivot
        a = eliminate(a, multi_by, i+1)
        
    return rearrange_rows(a)


# def solve(a):
#     sol = [] * len(a)
#     a = ref(a)
#     for i in range(n-1, -1, -1):
#         print(a[i])
#     return 
# print(solve(inp))
print(ref(inp))
