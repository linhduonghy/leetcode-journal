from typing import List
from math import ceil

def can_distribute(quantities: List[int], n: int, k: int):
    count = 0
    for quantity in quantities:
        number_of_stores = ceil(quantity / k)
        count += number_of_stores
    return count <= n
        
    
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l = 1
        r = max(quantities)
        ans = r
        while l <= r:
            mid = (l + r) // 2
            if can_distribute(quantities, n, mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
