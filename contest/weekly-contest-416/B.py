import math
from math import floor
from typing import List


def canReduceHeight(mountainHeight: int, workerTimes: List[int], mid: int):

    cnt = 0
    for workerTime in workerTimes:
        s = mid // workerTime
        cnt += floor((-1 + math.sqrt(1 + 8 * s)) / 2)  # find k : (1 + 2 + .. + k) <= s
        if cnt >= mountainHeight:
            return True
    return False


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        res = int(1e18)
        l = 1
        r = int(1e18)
        while l <= r:
            mid = (l + r) // 2
            if canReduceHeight(mountainHeight, workerTimes, mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res

if __name__ == '__main__':
    print(Solution().minNumberOfSeconds(3, [1]))