"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # sorted string alphabetically -> this is the key for this problem, since sorting in
        # this fashion keeps words with similar prefix closer to each other
        strs = sorted(strs)
        
        # here is the brilliant thing, after sorting, the first and the last will be the
        # most different
        first = strs[0]
        last = strs[-1]
        
        ret = ""
        # hence we only have to check the first and last
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ret
            ret += first[i]
        
        return ret
solution = Solution()
strs = ["dog","racecar","car"]

print(solution.longestCommonPrefix(strs))
#print(sorted(strs))