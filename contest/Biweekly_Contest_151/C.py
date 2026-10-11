from typing import List

class Solution:
    def minCost(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return max(nums)
        res = 0
        i = 0
        n = len(nums)
        while i < n - 2:
            tmp = nums[i:i + 3]
            tmp.sort()
            if  i + 3 == n - 1 and tmp[1] + tmp[2] < nums[i + 3] + tmp[2]:
                res += tmp[1]
                nums[i + 2] = tmp[-1]
            elif i + 3 < n and tmp[2] < nums[i + 3]:
                res += tmp[1]
                nums[i + 2] = tmp[2]
            else:
                res += tmp[2]
                nums[i + 2] = tmp[0]
            i += 2
            if i == n - 1:
                res += nums[-1]
            elif i == n - 2:
                res += max(nums[-1], nums[-2])
        return res