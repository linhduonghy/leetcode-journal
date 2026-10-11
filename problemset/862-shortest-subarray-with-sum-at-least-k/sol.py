from heapq import heappop, heappush
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        prefix_sum = 0
        sum_heap = []
        ans = len(nums) + 1
        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum >= k:
                ans = min(ans, i + 1)

            while sum_heap and prefix_sum + sum_heap[0][0] >= k:
                index = heappop(sum_heap)[1]
                ans = min(ans, i - index)

            heappush(sum_heap, (prefix_sum, i))

        return -1 if ans == (len(nums) + 1) else ans