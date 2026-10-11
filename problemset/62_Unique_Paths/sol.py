class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i + 1 < m: 
                    dp[i + 1][j] = dp[i][j] + 1
                if j + 1 < n:
                    dp[i][j + 1] = dp[i][j] + 1

        return dp[m - 1][n - 1]