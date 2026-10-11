from typing import List
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:

        n = len(nums)
        i, j = 0, 0
        freq = {}
        ans = 0
        while j < n:
            freq[nums[j]] = freq.get(nums[j], 0) + 1
            while max(freq) - min(freq) > 2:
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    del freq[nums[i]]
                i += 1
            ans += j - i + 1
            j += 1

        return ans




