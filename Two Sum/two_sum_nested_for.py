"""
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
"""

class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return None
            
nums = [2,7,11,15]
target = 9

solution = Solution()
print(solution.twoSum(nums, target))
