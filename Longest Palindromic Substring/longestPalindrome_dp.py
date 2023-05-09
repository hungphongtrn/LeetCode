'''
Given a string s, return the longest palindromic substring in s
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # the size of the string
        n = len(s)
    
        # initialize a 2D "state" matrix with row and vector are respectively the index of the string
        # state[i][j] == 1 if s[i:j] is a palindrome, == 0 if not
        state = [[0 for x in range(n)] for y in range(n)]
    
        # state[i][i] always = 1 - length - 1 string
        for i in range(n):
            state[i][i] = True
        
        # Check edge cases
        # all string with length 1 is palindrome
        longestLength = 1
        
        # check for substring with length 2
        longestStart = 0
        for i in range(n-1):
            if (s[i] == s[i+1]):
                state[i][i+1] = True
                longestStart = i
                longestLength = 2
        
        # with substring larger than 2
        # k will be used to update substring length
        for k in range(3, n+1):
            # Fix the starting index
            for i in range(n - k + 1):
                # Get the ending index of
                # substring from starting
                # index i and length k
                j = i + k - 1
     
                # checking for sub-string from
                # ith index to jth index if
                # st[i + 1] to st[(j-1)] is a
                # palindrome
                if (state[i + 1][j - 1] and s[i] == s[j]):
                    state[i][j] = True
                    if (k > longestLength):
                        longestStart = i
                        longestLength = k
                        
        print(longestStart)
        print(longestLength)
        return s[longestStart: longestStart + longestLength]
            
solution = Solution()
s = "cbbd"
print(solution.longestPalindrome(s))
    
    