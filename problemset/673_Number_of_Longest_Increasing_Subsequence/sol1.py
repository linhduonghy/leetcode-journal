class Solution:
    """
    """
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        counter = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        counter[i] = counter[j]
                    elif dp[j] + 1 == dp[i]:
                        counter[i] += counter[j]
        
        m = max(dp)
        count = 0
        for i in range(len(nums)):
            if dp[i] == m:
                count += counter[i]
        return count

        
