import math
from typing import List

def can_divide(nums: List[int], maxOperations: int, minBalls: int ) -> bool:

    for num in nums:
        if num <= minBalls:
            continue
        operations = (num - 1)  // minBalls
        maxOperations -= operations

        if maxOperations < 0:
            return False
    return True


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        l, h = 1, max(nums)
        while l <= h:
            mid = (l + h) // 2
            if can_divide(nums, maxOperations, mid):
                h = mid - 1
            else:
                l = mid + 1
        return l

if __name__ == '__main__':
    Solution().minimumSize([7,17], 2)