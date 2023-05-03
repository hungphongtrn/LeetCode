'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.        
class LinkedList:
    # customized to take in a list
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            # remove the first element of nodes and assign it to the first node of the linked list
            node = ListNode(val=nodes.pop(0))
            self.head = node
            # since we have popped the first element, we avoided repetition
            for elem in nodes: 
                node.next = ListNode(val = elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        nodes.append(None)
        return ' -> '.join(map(str, nodes))
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

# test linkedlist functionality
l1 = [9,9,9,9,9,9,9]
llist1 = LinkedList(l1)

l2 = [9,9,9,9]
llist2 = LinkedList(l2)

print(repr(llist1))
print(repr(llist2))    
        

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: List[int]
        :type l2: List[int]
        :rtype: List[int]
        """
        ret = ListNode()
        # Curr to keep track of current node 
        curr = ret
        carry = 0
        # if carry = 0 stop, else add 1 to the final node
        while l1 or l2 or carry: 
            val1 = l1.val if l1 else 0 # if not exist, will be 0
            val2 = l2.val if l2 else 0 
            
            sum = val1 + val2 + carry
            carry = sum // 10
            curr.next = ListNode(val = (sum%10))
            
            # continue to iterate to next of l1, l2 and curr
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        
        return ret.next
    '''
    since we update value to the next node instead of first node
    as we instantiate ret with ListNode, therefore the first value will be 0, 
    which will not belong to the final result
    '''        
        
        
solution = Solution()
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
ll1 = LinkedList(l1).head
ll2 = LinkedList(l2).head
ret = solution.addTwoNumbers(ll1,ll2)
node = ret
while node is not None:
    print(node.val)
    node = node.next
        
        