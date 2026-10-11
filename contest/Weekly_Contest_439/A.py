from typing import List
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        set_nums = set(nums)
        n = len(nums)
        ans = -1
        for num in set_nums:
            count_seg = 0
            for i in range(n - k + 1):
                contain = False
                for j in range(i, i + k):
                    if nums[j] == num:
                        contain = True
                        break
                if contain:
                    count_seg += 1
            if count_seg == 1:
                ans = max(ans, num)

        return ans