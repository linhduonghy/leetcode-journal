from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        n = len(nums)
        i = 0
        res = []
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                res.append(nums[i])
                nums[i + 1] *= 0
                i += 1
            i += 1

        res = res + [0] * (n - len(res))

        return res


