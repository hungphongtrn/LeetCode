# Two Sum Solution 
## Information 
* Date: 1/5/23 
* Difficulty: Easy
* Link: https://leetcode.com/problems/two-sum/
* Problem: \
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. \
You may assume that each input would have exactly one solution, and you may not use the same element twice. \
You can return the answer in any order.\
```
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```
```
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
```
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
```
## Solutions
### [Solution 1](https://github.com/yuufong/LeetCode/blob/main/Two%20Sum/two_sum_hash.py)
#### Thought Process
To solve this problem, we can use a hash table to store the numbers we have seen so far, and their indices. For each number in the array, we check if its complement (i.e. target - num) exists in the hash table. If it does, we have found the two numbers that add up to the target.
#### Complexity: $O(n)$

### [Solution 2](https://github.com/yuufong/LeetCode/blob/main/Two%20Sum/two_sum_nested_for.py)
#### Thought Process
To solve this problem, we can iterate over each pair of numbers in the input array nums, checking if their sum equals the target. To avoid using the same element twice, we start the second loop at the index i+1.

This approach is brute force and has a time complexity of O(n^2), which is not efficient for large input arrays. However, since the input size is small, this solution will work well.

We can improve this solution's time complexity by using a hash table to store the numbers we have seen so far, as we did in the previous solution.
#### Complexity: $O(n^2)$
### [Solution 3](https://github.com/yuufong/LeetCode/blob/main/Two%20Sum/two_sum_sliding_window.py)
#### Thought Process
This solution starts by sorting the input array nums to take advantage of the sorted order. We then set two pointers left and right to the beginning and end of the sorted array, respectively.

At each iteration of the while loop, we compute the sum of the two elements at the current left and right indices. If the sum is equal to the target, we use the index method to find the indices of these elements in the original nums array.

If the indices of the two elements are the same, we look for the second occurrence of the right element, starting from the index after the left element.

If the sum is less than the target, we increment the left pointer, since the sum can only increase by moving to a larger element. If the sum is greater than the target, we decrement the right pointer, since the sum can only decrease by moving to a smaller element.
#### Complexity: $O(nlog(n))$ due to initial sorting but $O(1)$ since we don't use any additional data structures


