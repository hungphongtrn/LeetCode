# Longest Common Prefix
## Information 
* Date: 12/5/23 
* Difficulty: Easy
* Link: 
* Problem: \
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
```
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
```
```
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

## Solutions
### [Solution 1]()
#### Thought Process
The key of this solution based on the function "sorted" of Python, which sorts the array **alphabetically**. Therefore, closer strings with similar prefix will be group together, hence the larger the positional gap is, the more different the prefix will be. Therefore, we will only compare the first and the last strings for the similar prefix.  
#### Complexity: $O(n)$ and $O(n)$ for space
