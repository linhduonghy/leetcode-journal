from typing import List
import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        gifts = [-x for x in gifts]
        heapq.heapify(gifts)
        
        while k > 0:
            top = math.floor(math.sqrt(-heapq.heappop(gifts)))
            heapq.heappush(gifts, -top)
            k -= 1
        
        return -sum(gifts)
        