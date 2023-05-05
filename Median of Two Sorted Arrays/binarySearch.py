def binarySearch(arr, target):
    '''
        Array is sorted, presumably in increasing order
    '''
    
    # left and right pointer
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # mid index, floor division
        mid = (left + right) // 2
        
        if target == arr[mid]:
            return mid
        
        elif target < arr[mid]:
            right = mid + 1
        
        elif target > arr[mid]:
            left = mid - 1
            
    return -1 

# test
print(binarySearch([1,3,4,5,6,7,9], 5))