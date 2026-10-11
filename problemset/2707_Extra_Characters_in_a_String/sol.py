from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        n = len(s)
        dictSet = set(dictionary)
        dp = [0 if s[:(i + 1)] in dictSet else 1 for i in range(n)]
        for i in range(1, n):
            if dp[i] == 0:
                continue
            dp[i] = dp[i - 1] + 1
            for k in range(1, i + 1):
                if s[k:i+1] in dictSet:
                    dp[i] = min(dp[i], dp[k - 1])
        return dp[-1]