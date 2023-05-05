# study purpose: Merge Sort implemenentation
def merge(arr, l, m, r):
    '''
        First subarray: arr[l:m]
        Second subarray: arr[m+1:r] 
    '''
    # size of each sub array
    n1 = m - l + 1
    n2 = r - m
    
    # create temp arrays
    L = [0] * n1
    R = [0] * n2
    
    # copy data to temp array
    for i in range(0, n1): L[i] = arr[l + i]
    for i in range(0, n2): R[i] = arr[m + 1 + i]
    
    # merge back temp arr (L & R) into arr
    i = 0 # first index of L array
    j = 0 # first index of R array
    k = l # first index of merged array
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        
    # copy the remaining
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k +=1 

def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
# Test 
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i],end=" ")