# Add two Numbers
## Information 
* Date: 3/5/23 
* Difficulty: Medium
* Link: https://leetcode.com/problems/add-two-numbers
* Problem: \
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
```
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```
```
Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
```
```
Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```
## Solutions
### [Solution 1](https://github.com/yuufong/LeetCode/blob/main/Add%20two%20Numbers/add_2_numb.py)
#### Thought Process
A elementary math problem that requires you to add 2 numbers, therefore, the easiest way is to add digit-by-digit. The sum of 2 digits might result in a carry of 0 or 1, which will be transfered to the sum of the next 2 digits. That's all.
However, implementation with the linked list data structure is the reason this elementary math is leveled as medium. I have made comments in my code regarding "coding" difficulty.
#### Complexity $O(max(len(l1||l2)))$
#### Comments
I have also made some basic functional LinkedList and ListNode class for easier visualization in my local machine.
