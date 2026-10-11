import math
from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0] * nums[0]
        res = 0
        gcd = math.gcd(*nums)
        lcm = math.lcm(*nums)
        res = max(res, lcm * gcd)
        for i in range(len(nums)):

            res = max(res, lcm * gcd)
            new_nums = nums[:i] + nums[i+1:]
            print(new_nums)
            gcd = math.gcd(*new_nums)
            lcm = math.lcm(*new_nums)
            print(gcd * lcm)
            res = max(res, lcm * gcd)

        return res

if __name__ == '__main__':
    Solution().maxScore([6,14,20])