from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums)
        nums = [int(x, 2) for x in nums]
        for num in range(0, (1 << n)):
            if num not in nums:
                return format(num, "0"+str(n)+"b")
        return ""
        