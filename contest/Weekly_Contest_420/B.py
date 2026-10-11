from typing import List

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        cnt = [[0] * 26 for i in range(n + 1)]

        for i in range(0, n):
            for c in range(0, 26):
                cnt[i + 1][c] = cnt[i][c]
            cnt[i + 1][ord(s[i]) - ord('a')] = cnt[i][ord(s[i]) - ord('a')] + 1

        count = 0
        for i in range(n):
            c = self.findFirstValidIndex(i, n, cnt, k)
            if c != -1:
                count += (n - c)
        return count

    def valid(self, i: int, j: int, cnt: List[List[int]], k:int):
        for c in range(0, 26):
            if cnt[j + 1][c] - cnt[i][c] >= k:
                return True
        return False

    def findFirstValidIndex(self, i: int, n: int, cnt: List[List[int]], k: int):

        l = i
        r = n - 1
        res = n
        while l <= r:
            mid = (l + r) // 2
            if self.valid(i, mid, cnt, k):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res if res != n else -1

if __name__ == '__main__':
    Solution().numberOfSubstrings("abcde", 1)