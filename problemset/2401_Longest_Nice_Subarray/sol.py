from typing import List

def is_nice_sub_array(nums: List[int], x: int, y: int) -> bool:
    bit_mask = 0
    for i in range(x, y + 1):
        if bit_mask & nums[i] != 0:
            return False
        bit_mask |= nums[i]
    return True

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 0
        res = 1
        while i < n:
            while j < n and is_nice_sub_array(nums, i, j): j += 1
            res = max(res, j - i)
            i += 1
        return res