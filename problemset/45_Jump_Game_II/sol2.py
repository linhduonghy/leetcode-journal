class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        jump = 0
        maxReach = 0
        milestone = 0

        for i in range(n - 1):
            maxReach = max(maxReach, i + nums[i])
            if milestone == i:
                milestone = maxReach
                jump += 1
        
        return jump
