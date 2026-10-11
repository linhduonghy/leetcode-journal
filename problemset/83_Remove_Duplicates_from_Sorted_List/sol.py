# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        cur = head
        prev = cur
        while cur is not None:
            if prev.val != cur.val:
                prev.next = cur
                prev = cur
            cur = cur.next
        prev.next = None
        return head