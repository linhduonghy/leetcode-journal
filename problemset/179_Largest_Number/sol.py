from typing import List
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a: str, b: str):
            return int(b + a) - int(a + b)
        
        nums = [str(x) for x in nums]
        
        nums.sort(key=cmp_to_key(compare))
        res = ''.join(nums)
        i = 0
        while res[i] == '0': i += 1
        
        return res[i]
        
        
        