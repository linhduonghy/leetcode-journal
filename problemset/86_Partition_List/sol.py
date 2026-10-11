# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessNode = ListNode(0)
        greaterNode = ListNode(0)
        headLessNode = lessNode
        headGreaterNode = greaterNode
        cur = head

        while cur is not None:
            if cur.val < x:
                lessNode.next = cur
                lessNode = lessNode.next
            else:
                greaterNode.next = cur
                greaterNode = greaterNode.next
            cur = cur.next

        greaterNode.next = None
        lessNode.next = headGreaterNode.next

        return headLessNode.next

