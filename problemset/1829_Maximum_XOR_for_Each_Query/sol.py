from typing import List

class Solution:
    
    """
        a xor b <= max(a, b)
        
        a xor b = c => a xor c = b
    """ 
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        maxV = (1 << maximumBit) - 1
        
        res = []
        cur = 0
        for num in nums:
            cur = cur ^ num
            res.append(cur ^ maxV)
        return res[::-1]
        