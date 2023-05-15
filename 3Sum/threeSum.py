"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # create the result set as ret
        ret = set()
        
        # create negative, positive, and zeros list 
        n, p, z = [], [], []
        for num in nums: 
            if num > 0: p.append(num)
            if num < 0: n.append(num)
            if num == 0: z.append(num)
        
        # create negative and positive set for O(1) look-up time
        N, P = set(n), set(p)
        
        # checking triplets that contain 0
        # more than 3 zero available --> is a result
        if len(z) >= 3: ret.add((0,0,0))
        # 1 zero in the tripet, find the complement of negative in the positive set
        if len(z) >= 1:
            for negative in N: 
                if -negative in P:
                    ret.add((0, negative, -negative))
                
        # checking triples that do not contain 0
        # using combinations from itertools to iterate faster
        from itertools import combinations
        
        # for the combinations of every 2 element in either negative or positive, find 
        # the complement of those sums to add into the result
        
        # checking the negative list
        for num1, num2 in combinations(n, 2): # find all combinations of pairs in negative list
            if -(num1 + num2) in P:
                ret.add(tuple(sorted([num1, num2, -(num1 + num2)])))
                
        # checking the positive list
        for num1, num2 in combinations(p, 2): # find all combinations of pairs in negative list
            if -(num1 + num2) in N:
                ret.add(tuple(sorted([num1, num2, -(num1 + num2)])))
        
        return ret
    
solution = Solution()

nums = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]

print(solution.threeSum(nums))