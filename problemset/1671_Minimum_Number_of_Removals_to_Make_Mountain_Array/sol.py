from typing import List

class Solution:
    
    """ Find the LIS from left to right and find LIS from right to left
    """
    def minimumMountainRemovals(sefl, nums: List[int]) -> int:
    
        n = len(nums)
        fl = [1] * n
        fr = [1] * n
        
        for i in range(1, n):
            for prev in range(0, i):
                if nums[i] > nums[prev]:
                    fl[i] = max(fl[i], fl[prev] + 1)
        
        for i in range(n - 2, -1, -1):
            for nxt in range(i + 1, n):
                if nums[i] > nums[nxt]:
                    fr[i] = max(fr[i], fr[nxt] + 1)
        
        max_len = 0
        for i in range(1, n - 1):
            if fl[i] == 1 or fr[i] == 1:
                continue
            max_len = max(max_len, fl[i] + fr[i] - 1)
        
        return n - max_len
            
                