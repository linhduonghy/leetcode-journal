from typing import List
import heapq

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def in_grid(x, y, m, n):
    return x >= 0 and y >= 0 and x < m and y < n

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        
        k = len(queries)
        m, n = len(grid), len(grid[0])
        queries_ordered = sorted([(q, index)  for index, q in  enumerate(queries)])
        result = [0] * k
        
        pq = [(grid[0][0], 0, 0)]
        heapq.heapify(pq)
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        cur_point = 0
        for query, index in queries_ordered:
            while pq and pq[0][0] < query:
                cur_point += 1
                smallest = heapq.heappop(pq)
                _, x, y = smallest[0], smallest[1], smallest[2]
                for dx, dy in direction:
                    x1, y1 = x + dx, y + dy
                    if in_grid(x1, y1, m, n) and not visited[x1][y1]:
                        visited[x1][y1] = True
                        heapq.heappush(pq, (grid[x1][y1], x1, y1))
            result[index] = cur_point
                
        return result