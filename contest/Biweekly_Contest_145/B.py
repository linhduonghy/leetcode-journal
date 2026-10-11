from typing import List

def can(strength: List[int], K: int, num_times: int) -> bool:

    if strength[-1] > num_times:
        return False

    n = len(strength)
    visited = [False] * n
    visited[-1] = True
    n -= 1
    energy = 0
    factor = K + 1
    num_times -= strength[-1] - 1
    for i in range(num_times):
        if n == 0:
            return True
        energy += factor
        for i in range(len(strength) - 1):
            if not visited[i] and energy >= strength[i]:
                visited[i] = True
                n -= 1
                energy = 0
                factor += K
                break


    return False

class Solution:
    def findMinimumTime(self, strength: List[int], K: int) -> int:

        strength.sort(reverse=True)
        l, r = 0, int(1e6 + 10)
        ans = int(1e9)
        while l <= r:
            mid = (l + r) // 2
            if can(strength, K, mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

if __name__ == '__main__':
    Solution().findMinimumTime([174874, 599667, 586782, 151292], 2)
