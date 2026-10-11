class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums())
        for i in range(1, n):
            if nums[i - 1] < i:
                return False
            nums[i] = self.max(nums[i] + i, nums[i - 1])
        return True
    def max(self, a: int, b: int) -> int:
        return a if a > b else b