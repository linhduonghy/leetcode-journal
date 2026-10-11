from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n - 2):
            if nums[i] == 1:
                continue
            for j in range(i, i + 3):
                nums[i] = 0 if nums[i] == 1 else 1
            cnt += 1
        if nums[-1] != 0 or nums[-2] != 0:
            return -1
        return cnt