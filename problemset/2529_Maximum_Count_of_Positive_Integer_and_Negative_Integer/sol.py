from typing import List
import bisect

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        left_zero = bisect.bisect_left(nums, 0)
        if left_zero < n and nums[left_zero] == 0:
            right_zero = bisect.bisect_right(nums, 0)
            right_zero -= 1
            return max(left_zero, n - right_zero - 1)

        if left_zero == n or left_zero == 0:
            return n

        return max(left_zero, n - left_zero)