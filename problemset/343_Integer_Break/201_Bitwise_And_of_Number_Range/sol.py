import math

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        if left == 0:
            return 0
        
        if (int(math.log2(left)) != int(math.log2(right))):
            return 0
        
        count = 0
        # count prefix commit bit 1
        while (left and left != right):
            left >>= 1
            right >>= 1
            count += 1
        
        return left << count