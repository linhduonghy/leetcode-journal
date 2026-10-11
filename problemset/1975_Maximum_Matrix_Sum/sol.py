from typing import List
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        negative_count = 0
        min_abs_value = 100000
        for row in matrix:
            for v in row:
                if v < 0:
                    negative_count += 1
                total += abs(v)
                min_abs_value = min(min_abs_value, abs(v))
        
        if negative_count % 2 == 1:
            total -= 2 * min_abs_value
        return total
                 
        