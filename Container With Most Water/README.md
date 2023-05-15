# Container With Most Water
## Information 
* Date: 12/5/23
* Difficulty: Medium
* Link: https://leetcode.com/problems/container-with-most-water/
* Problem: \
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
![Example 1]((https://github.com/yuufong/LeetCode/blob/main/Container%20With%20Most%20Water/question_11.jpg)
```
Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```
```
Example 2:

Input: height = [1,1]
Output: 1
```

## Solutions
### [Solution 1](https://github.com/yuufong/LeetCode/blob/main/Container%20With%20Most%20Water/maxArea.py)
#### Thought Process
1. Initialize two pointers, left and right, pointing to the first and last elements of the height array, respectively.
2. Initialize max_area variable to 0.
3. While left is less than right:
a. Calculate the current area as the minimum height between height[left] and height[right], multiplied by the distance between them.
b. Update max_area with the maximum of the current area and max_area.
c. Move the pointer that points to the smaller height inward, i.e., if height[left] is smaller, increment left by 1; otherwise, decrement right by 1.
Return max_area as the maximum amount of water the container can store.
#### Complexity $O(n)$ 
