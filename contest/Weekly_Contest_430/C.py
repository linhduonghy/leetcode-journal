from typing import List
from collections import defaultdict


def bs1(pairs: List[tuple[int]], x: int, fr: int, to: int) -> int:
    l = fr
    r = to
    ans = -1
    while l <= r:
        mid = (l + r) // 2

        if pairs[mid][0] > x:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans


def bs2(pairs: List[tuple[int]], y: int, fr: int, to: int) -> int:
    l = fr
    r = to
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if pairs[mid][0] < y:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans

class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:

        n = len(nums)
        pair_products = defaultdict(list)
        count = 0

        for i in range(n):
            for j in range(i + 2, n):
                product = nums[i] * nums[j]
                pair_products[product].append((i, j))

        for product, pairs in pair_products.items():
            pairs.sort()
            m = len(pairs)
            for x in range(m):
                p, r = pairs[x]
                fr = bs1(pairs, p + 1, x, m - 1)
                to = bs2(pairs, r - 1, x, m - 1)
                if fr == -1 or to == -1:
                    continue
                valid_count = sum(1 for idx in range(fr, to + 1) if pairs[idx][1] - r > 1)
                count += valid_count

        return count