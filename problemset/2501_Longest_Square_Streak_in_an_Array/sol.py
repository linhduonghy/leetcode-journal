from typing import List

import math


square_list = [] 
def build_square_list(limit: int):
    
    sqrt = math.sqrt(limit) 
    for i in range(2, int(sqrt) + 1, 1):
        square_list.append(i)
        square_list.append(i * i)
    
build_square_list(100000)

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        limit = max(nums)
        nums = set(nums)
        dp = {}
        for square in square_list:
            if square > limit:
                break
            dp[square] = 1 if square in nums else 0
        res = -1
        for square in square_list:
            s2 = square * square
            if square > limit:
                break
            if s2 in nums:
                dp[s2] = dp[square] + 1
                res = max(res, dp[s2])
        return -1 if res < 2 else res