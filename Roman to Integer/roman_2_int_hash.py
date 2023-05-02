"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
Given a roman numeral, convert it to an integer.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashTable = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        for i in range (len(s) - 1):
            #print(i)
            print(s[i])
            print(hashTable[s[i]])
            # if I is after V, X is after L/C or C is after D/M
            if hashTable[s[i]] < hashTable[s[i+1]]: 
                sum -= hashTable[s[i]]
            else:
                sum += hashTable[s[i]]

        return sum + hashTable[s[-1]] 
    # Need to add the last element since above condition will stop the iteration at the second last element 
    
# Test
s = "III"
solution = Solution()
print(solution.romanToInt(s))
