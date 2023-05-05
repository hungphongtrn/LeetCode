'''
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
    The overall run time complexity should be O(log (m+n)).
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # lengths of nums1 and nums2 as n and m
        n = len(nums1)
        m = len(nums2)
        
        # if nums1 has more than nums2, swap
        if n > m: return self.findMedianSortedArrays(nums2, nums1)
    
        # we will start first in nums1
        start, end = 0, n
        merged_mid = (m + n + 1) // 2
        
        while start <= end: 
            mid = (start + end) // 2
            # number of elements on the left of the middle in array 1
            left1_size = mid
            # remaining elements are on array 2 
            left2_size = merged_mid - mid
            
            # return the leftmost and rightmost w.r.t the middle element in both array 1 & 2
            # set overflow as -inf for left and inf for right
            left1 = nums1[left1_size - 1] if (left1_size > 0) else float('-inf') #if lef1_size = 0, there is no element on its left, hence -inf
            left2 = nums2[left2_size - 1] if (left2_size > 0) else float('-inf') #similar
            right1 = nums1[left1_size] if (left1_size < n) else float('inf') #if left1_size = n - 1, there is no element on its right, hence inf
            right2 = nums2[left2_size] if (left2_size < m) else float('inf') #similar
            
            # if correct partitioned, then
            if left1 <= right2 and left2 <= right1: 
                # if m and n is dividable by 2, average of two
                if (m + n) % 2 == 0: 
                    # max of left and min of right are 2 middles
                    return  (max(left1, left2) + min(right1, right2))/2.0
                return max(left1, left2) #or min(right1,right2) same value
            
            if (left1 > right2):
                #left 1 is too big, reduce mid
                end = mid - 1 
            if (left2 > right1): 
                #left 2 is too big, increase mid to reduct middle index of array 2
                start = mid + 1

solution = Solution()
arr1 = [-5, 3, 6, 12, 15]
arr2 = [-12, -10, -6, -3, 4, 10]
print(solution.findMedianSortedArrays(arr1,arr2))