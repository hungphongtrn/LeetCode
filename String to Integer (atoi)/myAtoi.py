"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
"""

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        
        Checkpoints:
        - Remove leading whitespace.
        - Check if the next character (if not already at the end of the string) is '-' or '+'. Positive by default.
        - Continue to read before encountering non-digit character or end of string
        - Convert to integers
        - >= 2**31-1 is 2**31-1 | <= -2**31 is -2**31-1
        """
        maxInt, minInt = 2**31 - 1 , -2**31
        result, startIdx, sign = 0,0,1
        cleanStr = s.lstrip()
        
        if not cleanStr: return result

        if cleanStr[startIdx] in ("-", "+"):
            sign = -1 if cleanStr[startIdx] == "-" else 1 
            startIdx += 1
        
        for i in range(startIdx, len(cleanStr)):
            char = cleanStr[i]
            if not char.isdigit():
                break
            else:
                # read note at the end confusing
                result = (result * 10) + int(char)

        if result * sign > maxInt:
            return maxInt
        elif result * sign <= minInt:
            return minInt
        
        return result * sign

    
s = "42"
solution = Solution()
print(solution.myAtoi(s))