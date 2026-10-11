from typing import List
import heapq
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        m, n = len(grid), len(grid[0])
        min_obstacles = [[float("inf") for i in range(n)] for j in range(m)]
        pq = [(grid[0][0], 0, 0)]
        heapq.heappush(pq, (grid[0][0], 0, 0))
        
        while pq:
            cur_obstacle, x, y = heapq.heappop(pq)
            if x == m - 1 and y == n - 1:
                return cur_obstacle
            
            for d in directions:
                x1, y1 = x + d[0], y + d[1]
                if x1 >= 0 and x1 < m and y1 >= 0 and y1 < n and cur_obstacle + grid[x1][y1] < min_obstacles[x1][y1]:
                    min_obstacles[x1][y1] = cur_obstacle + grid[x1][y1]
                    heapq.heappush(pq, (min_obstacles[x1][y1], x1, y1))
        
        return min_obstacles[m - 1][n - 1]