def binary_search(a, k):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = (lo+hi) // 2
        if a[mid] == k:
            return mid
        elif a[mid] < k:
            a = mid + 1
        else:
            hi = mid - 1

    return None


# print(binary_search([1,2,3,4,5,6,7], 4))


#all values a[i] (i<lo) are < k
#all values a[i] (i>hi) are >= k
def first_greater(a, k):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = (lo+hi) // 2
        if a[mid] < k:
            a = mid + 1
        else:
            hi = mid - 1

    return lo

# print(first_greater([10,20,30,47,59,1002], 50))


# SORTING
# 4 7 2 18 5 9 1 23 5 4 8 10

#BUBBLE SORT
import random
def bubble_sort(a):
    n = len(a)
    for end in range(n-1, 0,-1):
        for i in range(0, end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a

# best case: O(n^2)
# worst case: O(n^2)


# print(bubble_sort([random.randint(1, 1000) for i in range(50)]))


# SELECTION SORT

def selection_sort(a):
    n = len(a)
    for i in range(0, n-1):
        min_index = i
        for j in range(i+1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a

# best case: O(n^2)
# worst case: O(n^2)
# number of swaps will be less than bubble sort. number of swaps = n for selection sort
# number of swaps in bubble sort is ~n^2/2




# INSERTION SORT

def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        k = a[i]
        j = i - 1

        while j >= 0 and k < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = k
    return a
# WORST CASE: O(n^2)
# best case: O(n)


print(insertion_sort([random.randint(1, 1000) for i in range(50)]))


# MERGE SORT


