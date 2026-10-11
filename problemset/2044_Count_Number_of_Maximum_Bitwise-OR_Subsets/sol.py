from typing import List

class Solution:

    def __init__(self) -> None:
        self.count = 0
        self.max_or = 0
    def genSubset(self, nums: List[int], cur: int, cur_or: int):
        if cur == len(nums):
            if self.max_or == cur_or:
                self.count += 1
            return
        self.genSubset(nums, cur + 1, cur_or | nums[cur])
        self.genSubset(nums, cur + 1, cur_or)
        
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        for num in nums:
            self.max_or = self.max_or | num
        self.genSubset(nums, 0, 0)
        
        return self.count