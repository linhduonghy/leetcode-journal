from functools import lru_cache


class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:

        def cost(c1: str, c2: str) -> int:
            diff = abs(ord(c1) - ord(c2))
            return min(diff, 26 - diff)

        @lru_cache(None)
        def dp(i: int, j: int, ops: int):
            if i > j:
                return 0
            if i == j:
                return 1
            best = max(dp(i, j - 1, ops), dp(i + 1, j, ops))
            c = cost(s[i], s[j])
            if c <= ops:
                best = max(best, 2 + dp(i + 1, j - 1, ops - c))
            return best

        return dp(0, len(s) - 1, k)
