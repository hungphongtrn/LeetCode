# Reverse Integer
## Information 
* Date: 8/5/23
* Difficulty: Medium
* Link: https://leetcode.com/problems/reverse-integer/
* Problem: \
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
```
Example 1:

Input: x = 123
Output: 321
```
```
Example 2:

Input: x = -123
Output: -321
```
```
Example 3:

Input: x = 120
Output: 214.
```
## Solutions
### [Solution 1]()
#### Thought Process
I think this is a fairly simple problem. I just convert the integer into a string, then read it from the back, add a minus at the start if it is negative. Another approach might be extracting each digit by dividing by 10 and take the surplus, reverse it. 
#### Complexity $O(n)$ 


