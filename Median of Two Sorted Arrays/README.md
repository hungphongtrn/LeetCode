# Longest Substring Without Repeating Characters 
## Information 
* Date: 5/5/23 
* Difficulty: Hard
* Link: https://leetcode.com/problems/median-of-two-sorted-arrays
* Problem: \
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be $O(log (m+n))$
```
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```
```
Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

## Solutions
### [Solution 1]()
#### Thought Process
At first, I planned to use the merge part of Merge Sort to solve this problem. However, I realize that the complexity for that will be linear as $O(m + n)$. The required complexity of $O(log (m+n))$ suggested me to use binary search to deal with it. 
Well, to be a little bit more truthful, I was stuck at that point - "Binary Search", so I needed a little push from [GeeksforGeeks](https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/)
#### Complexity: $O(log (m+n))$ and $O(1)$ for space
