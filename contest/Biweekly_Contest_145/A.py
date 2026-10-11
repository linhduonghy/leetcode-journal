from collections import Counter
from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        if min(nums) < k:
            return -1

        freq = Counter(nums)

        return len(freq) - 1 if min(nums) == k else len(freq)

