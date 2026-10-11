from typing import List

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def count(x: int):
            x = str(x)
            n = len(x) - len(s)
            if n < 0:
                return 0            
            dp = [[0] * 2 for _ in range(n + 1)]
            dp[n][0] = 1
            dp[n][1] = 1 if x[n:] >= s else 0
            for i in range(n - 1,-1,-1):
                digit = int(x[i])
                dp[i][0] = (1 + limit) * dp[i + 1][0]
                if digit > limit:
                    dp[i][1] = (1 + limit) * dp[i + 1][0]
                else:
                    dp[i][1] = digit * dp[i + 1][0] + dp[i + 1][1]
            return dp[0][1]
        
        return count(finish) - count(start - 1)