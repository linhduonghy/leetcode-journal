from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        for i in range(k):
            index = nums.index(min(nums))
            nums[index] *= multiplier

        return nums

if __name__ == "__main__":
    s = Solution()
    print(s.getFinalState([2,1,3,5,6], 5, 2))