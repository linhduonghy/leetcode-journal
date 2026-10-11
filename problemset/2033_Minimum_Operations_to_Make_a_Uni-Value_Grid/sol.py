from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = [x for g in grid for x in g]
        arr.sort()
        median_value = arr[len(arr) // 2]
        ans = 0
        for item in arr:
            if (item - median_value) % x != 0:
                return -1
            ans += abs(item - median_value) // x
        return ans