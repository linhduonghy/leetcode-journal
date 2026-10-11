from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [[0] * 2 for _ in range(n)]        
        dp[-1][1] = questions[-1][0]
        for i in range(n - 2, -1, -1):            
            dp[i][0] = max(dp[i + 1])
            dp[i][1] = questions[i][0]
            if i + questions[i][1] + 1 < n:
                dp[i][1] += max(dp[i + questions[i][1] + 1])
        return max(dp[0])
        