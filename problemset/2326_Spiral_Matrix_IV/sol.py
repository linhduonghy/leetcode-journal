# Definition for singly-linked list.

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        def getAndShift(head: Optional[ListNode]):
            if not head:
                return -1, None
            val = head.val
            head = head.next
            return val, head
        
        res = [[0 for _ in range(n)] for _ in range(m)]
        curX, curY = 0, 0
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        border = [0, n - 1, m - 1, 0]
        d = 0
        
        while True:

            if border[0] > border[2] or border[3] > border[1]:
                break
            while curX >= border[0] and curX <= border[2] and curY >= border[3] and curY <= border[1]:
                val, head = getAndShift(head)
                res[curX][curY] = val
                curX, curY = curX + direction[d][0], curY + direction[d][1]
             
            curX, curY = curX - direction[d][0], curY - direction[d][1]                
            if d == 1 or d == 2:
                border[d] -= 1
            else:
                border[d] += 1
            d = (d + 1) % 4
            curX, curY = curX + direction[d][0], curY + direction[d][1]
        
        return res