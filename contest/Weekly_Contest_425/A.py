from typing import List
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        ans = 100000
        n = len(nums)
        s = [0] * len(nums)
        s[0] = nums[0]
        for i in range(1, n):
            s[i] = s[i - 1] + nums[i]
        for i in range(n):
            for size in range(l, r + 1):
                if i + size - 1 >= n:
                    break
                _s = s[i + size - 1]
                if i > 0:
                    _s -= s[i - 1]
                print(i, size, _s)
                if _s > 0:
                    ans = min(ans, _s)

        return -1 if ans == 100000 else ans