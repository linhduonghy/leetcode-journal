from typing import List
from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        n = len(nums)
        left = 0
        right = 1
        count[nums[0]] = 1
        cur = 0
        ans = 0
        while right < n:
            while right < n and cur < k:
                cur += count[nums[right]]
                count[nums[right]] += 1
                right += 1
            if cur >= k:
                ans += (n - right + 1)
            count[nums[left]] -= 1
            cur -= count[nums[left]]
            left += 1
        while left < right and cur >= k:
            ans += 1
            count[nums[left]] -= 1
            cur -= count[nums[left]]
            left += 1
            
        return ans
                