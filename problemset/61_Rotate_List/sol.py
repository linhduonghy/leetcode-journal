# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def size(head: Optional[ListNode]):
    cur = head
    sz = 0
    while cur is not None:
        sz += 1
        cur = cur.next
    return sz


def rotate(head: Optional[ListNode]):
    cur = head
    prev = None
    while cur.next is not None:
        prev = cur
        cur = cur.next
    prev.next = None
    cur.next = head
    return cur

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        n = size(head)
        if n == 0:
            return head
        k = k % n
        if k == 0:
            return head

        cur = head
        prev = None
        while k < n:
            k += 1
            prev = cur
            cur = cur.next
        prev.next = None

        head1 = cur
        while cur.next is not None:
            cur = cur.next
        cur.next = head
        return head1

