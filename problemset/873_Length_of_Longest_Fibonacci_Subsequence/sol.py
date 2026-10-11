from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                dp[i][j] = 2
        
        val_idx = {val: idx for idx, val in enumerate(arr)}
        
        max_len = 0
        for prev in range(1, n - 1):
            for next in range(prev + 1, n):
                diff = arr[next] - arr[prev]
                diff_idx = val_idx.get(diff, None)
                if not diff_idx and diff_idx < prev:
                    dp[prev][next] = dp[diff_idx][prev] + 1
                    max_len = max(max_len, dp[prev][next])
        
        return max_len if max_len > 2 else 0
                