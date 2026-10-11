class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)

        dp = [n + 1 for i  in range(n)]
        maxJ = [0 for i in range(n)]
        dp[0] = 0
        maxJ[0] = nums[0]
        for i in range(1, n):
            k = -1
            for j in range(n):
                if maxJ[j] >= i:
                    k = j
                    break
            if k == -1:
                return -1
            
            dp[i] = k + 1
            maxJ[dp[i]] = max(maxJ[dp[i]], nums[i] + i)
        return dp[n - 1]
