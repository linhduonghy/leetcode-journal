from typing import List
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:

        n = len(nums)
        i = 0

        res = 0
        while i < n - 1:

            j = i + 1
            while j < n - 1 and nums[j] < nums[i]: j += 1
            res += (j - i) * nums[i]
            i = j

        return res

if __name__ == '__main__':
    Solution().findMaximumScore([4,3,1,3,2])