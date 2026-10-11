from typing import List
from math import gcd


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:

        print(nums)
        n = len(nums)
        g = [[0] * n for i in range(n)]

        for i in range(n - 1):
            g[i][i] = nums[i]
            for j in range(i + 1, n):
                g[i][j] = gcd(g[i][j - 1], nums[j])
        print(g)
        res = 0

        def find_left_gcd_equal(left: int, target: int):
            l = left
            r = n - 1
            pos = n
            while l <= r:
                mid = (l + r) // 2
                if g[left][mid] == target:
                    pos = min(pos, mid)
                    r = mid - 1
                elif g[left][mid] < target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1 if pos == n else pos

        def find_right_gcd_equal(left: int, target: int):
            l = left
            r = n - 1
            pos = -1
            while l <= r:
                mid = (l + r) // 2
                if g[left][mid] == target:
                    pos = max(pos, mid)
                    l = mid + 1
                elif g[left][mid] < target:
                    r = mid - 1
                else:
                    l = mid + 1
            return pos

        for i in range(n - 1):
            for j in range(i, n):
                cur = g[i][j]
                for k in range(j + 1, n):
                    zmin = find_left_gcd_equal(k, cur)
                    zmax = find_right_gcd_equal(k, cur)
                    print(i, j, cur, k, zmin, zmax)
                    if zmin != -1:
                        res = (res + (zmax - zmin + 1) * 2) % 1000000007
            print(i, res)
        print(res)
        return res


if __name__ == '__main__':
    Solution().subsequencePairCount([1, 2, 3, 4])
