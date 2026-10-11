from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        n = len(weights)
        pair_weights = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]
        pair_weights.sort()
        
        ans = 0
        for i in range(k - 1):
            ans += pair_weights[n - i - 2] - pair_weights[i]
        
        return ans