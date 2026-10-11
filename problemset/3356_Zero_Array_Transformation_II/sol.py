from typing import List


def is_possible(nums: List[int], queries: List[List[int]], mid: int):

    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(mid):
        l, r, val = queries[i]
        prefix_sum[l] += val
        prefix_sum[r + 1] -= val

    if prefix_sum[0] < nums[0]:
        return False
    for i in range(1, n):
        prefix_sum[i] += prefix_sum[i - 1]
        if prefix_sum[i] < nums[i]:
            return False
    return True

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        l = 0
        r = len(queries)
        res = r + 1
        while l <= r:
            mid = (l + r) // 2
            if is_possible(nums, queries, mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return -1 if res == len(queries) + 1 else res
