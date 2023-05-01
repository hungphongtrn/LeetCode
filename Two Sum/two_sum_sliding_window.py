"""
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
"""
class Solution(object):
    def twoSum(self, nums, target):
        nums_sorted = sorted(nums)
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums_sorted[left] + nums_sorted[right]
            if current_sum == target:
                i, j = nums.index(nums_sorted[left]), nums.index(nums_sorted[right])
                if i == j: j = nums.index(nums_sorted[right], i + 1)
                return [i, j]
            elif current_sum < target: left += 1
            else: right -= 1
        return None




nums = [2,7,11,15]
target = 9

solution = Solution()
print(solution.twoSum(nums, target))