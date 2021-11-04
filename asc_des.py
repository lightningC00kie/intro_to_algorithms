def asc_des(a):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = (lo+hi)//2
        if a[mid-1] < a[mid] > a[mid+1]:
            return a[mid]
        
        elif a[mid] > a[mid-1]:
            lo = mid + 1

        elif a[mid] > a[mid+1]:
            hi = mid - 1

print(asc_des([10, 20, 30, 29, 5, 1]))