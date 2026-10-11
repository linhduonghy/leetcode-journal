from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] <= nums[j + 1]:
                    continue
                else:
                    if bin(nums[j]).count("1") == bin(nums[j + 1]).count("1"):
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    else:
                        return False
        
        return True