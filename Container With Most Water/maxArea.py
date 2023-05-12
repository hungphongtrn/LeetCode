"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        
        area = min(i,j) * (i-j) -> find i, j in height to max area
        """

        # initalize two pointers and max_area var
        left = 0 
        right = len(height) - 1
        max_area = 0
        
        while left < right: 
            print(left, right)
            max_area = max((min(height[left], height[right]))*(right - left), max_area)
            if height[left] < height[right]: 
                left += 1 # change pointer at which height is smaller
            else: 
                right -= 1 
            
        return max_area
    
solution = Solution()
height = [1,8,6,2,5,4,8,3,7]

print(solution.maxArea(height))
        
        
        
        
        
        