from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        operations = 0
        while True:

            n = len(nums)
            ok = True
            min_sum = float("inf")
            pos = -1
            for i in range(n - 1):
                if nums[i] > nums[i + 1]:
                    ok = False
                if nums[i] + nums[i + 1] < min_sum:
                    pos = i
                    min_sum = nums[i] + nums[i + 1]
            if ok:
                break
            operations += 1
            nums[pos] = min_sum
            for i in range(pos + 1, n - 1):
                nums[i] = nums[i + 1]
            nums.pop()

        return operations

