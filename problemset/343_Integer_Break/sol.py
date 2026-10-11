class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n == 2:
            return 1
        
        if n == 3:
            return 2
        
        dp = [0 for __ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i] = 1

        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if j >= i:
                    dp[j] = max(dp[j], i * dp[j - i])
        
        return dp[n]
        
            