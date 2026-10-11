from typing import List 
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        arr = [(int(s.split(":")[0]), int(s.split(":")[1])) for s in timePoints]
        
        arr.sort(key=lambda x : (x[0], x[1]))
        
        res = 24 * 60
        for i in range(0, len(arr) - 1):
            cur = arr[i]
            nxt = arr[i + 1]
            
            diffClockwise = nxt[0] * 60 + nxt[1] - cur[0] * 60 - cur[1] 
            res = min(res, diffClockwise, 24 * 60 - diffClockwise)
        
        cur = arr[0]
        nxt = arr[-1]
        diffClockwise = nxt[0] * 60 + nxt[1] - cur[0] * 60 - cur[1] 
        res = min(res, diffClockwise, 24 * 60 - diffClockwise)
                
        return res