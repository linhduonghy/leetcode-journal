from typing import List
import math
def can_repair(ranks: List[int], cars: int, time: int) -> bool:
    
    count = 0
    for rank in ranks:
        count += int(math.sqrt(time / rank))
        if count >= cars:
            return True
    return False
    
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        low = 1
        high = max(ranks) * cars * cars
        res = -1
        while low <= high:
            mid = (low + high) // 2
            if can_repair(ranks, cars, mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res
        