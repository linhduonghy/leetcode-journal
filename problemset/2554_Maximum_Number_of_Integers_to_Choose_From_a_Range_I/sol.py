from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        banned = set(banned)        
        curSum = 0
        res = 0
        for i in range(n):
            if curSum + i + 1 > maxSum:
                break
            if (i + 1) not in banned:
                curSum += i + 1
                res += 1
        
        return res
         
                