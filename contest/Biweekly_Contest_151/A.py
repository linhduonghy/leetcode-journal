from typing import List
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:

        cnt = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                cnt += 1

        return [0] * cnt + [1] * (len(nums) - cnt)