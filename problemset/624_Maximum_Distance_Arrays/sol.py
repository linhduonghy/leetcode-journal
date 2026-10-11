from typing import List
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:        
        
        minV = arrays[0][0]
        maxV = arrays[0][-1]
        
        maxDistance = 0
        
        for i in range(1, len(arrays)):
            maxDistance = max(maxDistance, abs(minV - arrays[i][-1]), abs(maxV - arrays[i][0]))
            minV = min(minV, arrays[i][0])
            maxV = max(maxV, arrays[i][-1])
            
        return maxDistance
            
