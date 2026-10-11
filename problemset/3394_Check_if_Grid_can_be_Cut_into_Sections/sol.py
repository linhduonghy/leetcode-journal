from typing import List

def checkValid(points: List[List[int]]) -> bool:
    cnt = 0
    max_prev = points[0][1]
    for i in range(1, len(points)):
        if points[i][0] >= max_prev:
            cnt += 1
        max_prev = max(max_prev, points[i][1])
    return cnt >= 2
    
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        horizontal_points = [ [rec[1], rec[3]] for rec in rectangles]
        vertical_points = [ [rec[0], rec[2]] for rec in rectangles]
        
        horizontal_points.sort(key = lambda x : x[0])
        vertical_points.sort(key = lambda x : x[0])
        return checkValid(horizontal_points) or checkValid(vertical_points)        
        