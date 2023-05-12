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