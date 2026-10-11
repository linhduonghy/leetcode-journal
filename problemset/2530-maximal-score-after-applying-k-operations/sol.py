import heapq
import math
from typing import List
from heapq import heappush, heappop

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        nums = [-x for x in nums]
        heapq.heapify(nums)

        res = 0
        while k > 0:
            top = heappop(nums)
            res += top
            heappush(nums, -math.ceil(-top / 3))
            k -= 1

        return -res
        