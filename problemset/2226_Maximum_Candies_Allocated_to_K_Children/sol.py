from typing import List


def is_possible(candies: List[int], mid: int, k: int) -> bool:
    count = 0
    for candy in candies:
        count += candy // mid
        if count >= k:
            return True
    return False

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low = 0
        high = 10 ** 7
        res = 0
        while low <= high:
            mid = (low + high) // 2
            if is_possible(candies, mid, k):
                low = mid + 1
                res = mid
            else:
                high = mid - 1

        return res