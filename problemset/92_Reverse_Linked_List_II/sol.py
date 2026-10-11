# Definition for singly-linked list.

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head
        
        cur = head
        cnt = 1
        lastLeftSide = None
        while cnt < left:
            cnt += 1
            lastLeftSide = cur
            cur = cur.next            

        continueNodeFromRight = cur 
        prev1 = None
        while cnt <= right:
            cnt += 1
            tmpNext = cur.next
            cur.next = prev1
            prev1 = cur
            cur = tmpNext

        continueNodeFromRight.next = cur
        if left == 1: 
            return prev1
        else:
            lastLeftSide.next = prev1
            return head