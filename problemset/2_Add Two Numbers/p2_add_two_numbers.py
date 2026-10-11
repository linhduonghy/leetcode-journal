# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = 0
        root = ListNode()
        currentNode = root
        while l1 is not None or l2 is not None:
            x = 0 if l1 is None else l1.val
            y = 0 if l2 is None else l2.val
            s = x + y + r
            r = 0 if s < 10 else 1
            s = s if s < 10 else s - 10
            
            currentNode.next = ListNode(s)
            currentNode = currentNode.next

            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
        
        if r > 0:
            currentNode.next = ListNode(r)
        return root.next
    
# 9999999
# 0009999
# 10009998 