# Definition for singly-linked list.

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def size(head: ListNode):
    if head is None:
        return 0
    return 1 + size(head.next)


def subNode(head: ListNode, n: int):
    if n == 0:
        return None, head

    cur = head
    for _ in range(n - 1):
        cur = cur.next

    temp = cur.next
    cur.next = None
    return head, temp


class Solution:

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = size(head)

        average = n // k
        numberOfPlusOne = n % k

        res = []
        for i in range(k):
            subSize = average + (1 if i < numberOfPlusOne else 0)
            subN, head = subNode(head, subSize)
            res.append(subN)

        return res
