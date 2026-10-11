from typing import List
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        n = len(nums)
        sum = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            sum[i] = (sum[i + 1] + nums[i]) % p
        if sum[0] == 0:
            return 0
        
        diff = sum[0] - p
        res = n
        rightPos = {0: n}
        for i in range(n - 1, -1, -1):
            x = (sum[i] - diff) % p
            if x in rightPos:
                res = min(res, rightPos[x] - i)
            rightPos[sum[i]] = i
        return -1 if res == n else res
    
if __name__ == "__main__":
    Solution().minSubarray([26,19,11,14,18,4,7,1,30,23,19,8,10,6,26,3], 26)