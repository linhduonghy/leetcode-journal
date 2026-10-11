from typing import List

def isPossible(arr: List[int], d: int, k: int) -> bool:
    cur = arr[0]
    n = len(arr)
    for i in range(1, n):
        if cur + k > arr[i] + d:
            return False
        cur = max(arr[i], cur + k)
    return True

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        l, r = 0, int(1e10)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if isPossible(start, d, mid):
                res =  mid
                l = mid + 1
            else:
                r = mid - 1
        return res


if __name__ == '__main__':
    Solution().maxPossibleScore(start=[6,0,3], d=2)