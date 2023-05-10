"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

"""

"""
isMatch("aab", "c*a*b") → true if we treat c* is 0 times appearing, a* twice and b
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str -> input string
        :type p: str -> pattern string
        :rtype: bool
        
        '.' <=> every single char
        '*' <=> any preceding character * k (k is 0, 1, 2 ... any thing you like)
        """
        # if p is empty return if s is also empty
        if not p: 
            return not s
        
        # if text is not empty and the character of patter is "." or match char at similar position in text
        match_char = bool(s) and p[0] in {s[0], '.'}
        
        # start recursion
        # the 1st recursive call skip the * char and its preceding char <=> matching zero instances
        # the 2nd recursive call 
        if len(p) >= 2 and p[1] == "*":
            return (self.isMatch(s, p[2:]) or 
                    match_char and self.isMatch(s[1:], p))
        else:
            # checking next character of the the string and pattern
            return match_char and self.isMatch(s[1:], p[1:])
        
                
solution = Solution()
s = "ab"
p = ".*"
print(solution.isMatch(s, p))
