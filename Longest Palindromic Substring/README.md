# Longest Substring Without Repeating Characters 
## Information 
* Date: 6/5/23 
* Difficulty: Medium
* Link: https://leetcode.com/problems/longest-palindromic-substring
* Problem: \
Given a string s, return the longest palindromic substring in s.
```
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```
```
Example 2:
Input: s = "cbbd"
Output: "bb"
```

## Solutions
### [Solution 1](https://github.com/yuufong/LeetCode/blob/main/Longest%20Substring%20Without%20Repeating%20Characters%20/long_sub_wo_rep.py)
#### Thought Process
To improve over the brute force solution, we first observe how we can avoid unnecessary re-computation while validating palindromes. Consider the case "ababa". If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two left and right end letters are the same.
#### Complexity: $O(n)$ and $O(n)$ for space
### Solution 2
#### Thought Process: [Manacher's Algorithm](https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/) 
In process
#### Comlexity: $O(n)$

### Solution 3
#### Thought Process: [Palindromic Tree](https://www.geeksforgeeks.org/longest-palindromic-substring-using-palindromic-tree-set-3/)
In process
#### Comlexity: $O(kn) ~ O(n)$
