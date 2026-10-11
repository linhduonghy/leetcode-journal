from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        max_rows = 0
        
        for cur_row in matrix:
            
            flip_row = [1 - x for x in cur_row]
            
                
            count = 0
            for row in matrix:
                if row == cur_row or row == flip_row:
                    count += 1

            max_rows = max(max_rows, count)
            
        return max_rows
        