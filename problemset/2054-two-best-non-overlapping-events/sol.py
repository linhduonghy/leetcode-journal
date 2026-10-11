import heapq
from typing import List
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:

        pq = []
        events.sort(key=lambda x: x[0])

        max_sum = 0

        for event in events:
            max_v = 0
            while pq and event[0] > pq[0][0]:
                max_v = max(max_v, pq[0][1])
                heapq.heappop(pq)
            max_sum = max(max_sum, max_v + event[2])
            heapq.heappush(pq, (event[1], event[2]))

        return max_sum
