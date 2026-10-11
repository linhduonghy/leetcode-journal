from typing import List
from collections import Counter
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:

        total = sum(nums)
        count = Counter(nums)
        res = float("-inf")
        for i in range(len(nums)):
            total_remain = total - nums[i]
            if total_remain % 2 != 0:
                continue
            count[nums[i]] -= 1
            # print(nums[i], total_remain, count[total_remain // 2])
            total_remain //= 2
            if count[total_remain] > 0:
                res = max(res, nums[i])
            count[nums[i]] += 1
        # print(res)
        return res

if __name__ == '__main__':
    s = Solution()
    s.getLargestOutlier([-108,-108,-517])