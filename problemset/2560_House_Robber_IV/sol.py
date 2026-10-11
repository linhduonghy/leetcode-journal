from typing import List


def is_possible(nums: List[int], mid: int, k: int):
    
    cnt = 0
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] <= mid:
            cnt += 1
            i += 2
        else:
            i += 1
        if cnt >= k:
            return True
    return False
    
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        
        mi = float("inf")
        ma = float("-inf")
        for num in nums:
            mi = min(mi, num)
            ma = max(ma, num)
        low = mi
        high = ma
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if is_possible(nums, mid, k):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans