from typing import List
import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        nums = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(nums)
        
        ans = 0
        visited = set()
        while nums:
            mi = heapq.heappop(nums)
            if mi[1] in visited:
                continue
            ans += mi[0]
            visited.add(mi[1])
            visited.add(mi[1] + 1)
            visited.add(mi[1] - 1)
        return ans        