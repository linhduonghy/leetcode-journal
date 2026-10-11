# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        prev = head
        head = head.next

        while head and head.next != None:
            if count + 1 == k:
                pass
            nxt = head.next

        return head

def addNode(node: ListNode, x: int):
    nextNode = ListNode(x)
    node.next = nextNode
    node = node.next
    return node

if __name__ =='__main__':
    lst = [1,2,3,4,5]
    k = 2

    head = ListNode(lst[0])
    cur = head
    for x in lst[1:]:
        cur = addNode(cur, x)
    
    sol = Solution()
    sol.reverseKGroup(head, k)
    

    