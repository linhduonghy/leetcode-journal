from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        mod = 1000000007
        n = len(arr)
        dp = [[0] * 2 for _ in range(n)]
        if arr[0] % 2 == 0:
            dp[0][0] = 1
        else:
            dp[0][1] = 1
        for i in range(1, n):
            if arr[i] % 2 == 0:
                dp[i][0] = (dp[i - 1][0] + 1) % mod
                dp[i][1] = dp[i - 1][1]
            else:
                dp[i][1] = (dp[i - 1][0] + 1) % mod
                dp[i][0] = dp[i - 1][1]
        
        cnt = 0
        for i in range(n):
            cnt = (cnt + dp[i][1]) % mod

        return cnt
    