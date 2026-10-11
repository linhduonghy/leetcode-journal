# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional

def gcd(a : int, b: int) -> int:
    if a == 0: return b
    return gcd(b % a, a)

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        prev = None
        while head.next is not None:
            prev = head
            head = head.next
            mid = ListNode(gcd(prev.val, head.val))
            prev.next = mid
            mid.next = head
        return res    
                
        