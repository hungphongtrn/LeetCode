# Longest Substring Without Repeating Characters 
## Information 
* Date: 4/5/23 
* Difficulty: Medium
* Link: 
* Problem: \
Given a string s, find the length of the longest substring without repeating characters
```
Example 1
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```
```
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
```
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```
## Solutions
### [Solution 1]()
#### Thought Process
One possible approach to solve this problem is by using a sliding window technique. We can use two pointers, left and right, to define a substring. By moving these pointers, we can iterate through the string and check for repeating characters.
#### Complexity: $O(n)$ and $O(n)$ for space
