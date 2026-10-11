from operator import itemgetter
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        maxx = max(nums)
        i = 0
        n = len(nums)
        res = 1
        while i < n:
            j = i
            while j < n and nums[j] == maxx: j += 1
            res = max(res, j - i)
            if j == i: j += 1
            i = j
        return res




