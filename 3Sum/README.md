# 3Sum
## Information 
* Date: 15/5/23
* Difficulty: hard
* Link: https://leetcode.com/problems/3sum
* Problem: \
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
```
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```
```
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```
```
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```
## Solutions
### [Solution 1](https://github.com/yuufong/LeetCode/blob/main/3Sum/threeSum.py)
#### Thought Process
The solution is around find the complement of the either a number or a sum of a pair. Therefore, first divide the list of nums into zeros, negative, and positive numbers lists. First we check the case if there're 1 zero in a triplets, finding two numbers, each from negative and positive lists, which are complementary. We continue checking for the triplets containing 3 zeros. Finally, we find the complement of every combinations of 2 elements that either come from negative or positive lists.
#### Complexity $O(n^2)$ 
