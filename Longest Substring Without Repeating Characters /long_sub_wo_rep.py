'''
    Given a string s, find the length of the longest substring without repeating characters
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        # chars used to stored "seen" character
        chars = [0] * 128
 
        left = right = 0
 
        res = 0
        while right < len(s):
            r = s[right]
            # ord(r) to convert char into 
            chars[ord(r)] += 1
 
            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1
 
            res = max(res, right - left + 1)
 
            right += 1
        return res    
    
    
s = "pwwekw"

solution = Solution()
print(solution.lengthOfLongestSubstring(s))
