from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        m, n = len(points), len(points[0])
        
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            dp[0][i] = points[0][i]
                        
        for i in range(0, m - 1):
            # calculate maxL, maxR
            maxL = [-1e5 for i in range(n)]
            maxR = [-1e5 for i in range(n)]
            maxL[0] = dp[i][0]
            maxR[n - 1] = dp[i][n - 1] - (n - 1)
            for j in range(1, n):
                maxL[j] = max(maxL[j - 1], dp[i][j] + j)
            for j in range(n - 2, -1, -1):
                maxR[j] = max(maxR[j + 1], dp[i][j] - j)
            
            for j in range(n):
                dp[i + 1][j] = max(dp[i + 1][j], max(maxL[j] - j + points[i + 1][j], maxR[j] + j + points[i + 1][j]))
            
        maxPoint = dp[m - 1][0]
        for j in range(1, n):
            maxPoint = max(maxPoint, dp[m - 1][j])
            
        return maxPoint
    
if __name__ == "__main__":
    s = Solution()
    s.maxPoints([[1,5],[2,3],[4,2]])
    