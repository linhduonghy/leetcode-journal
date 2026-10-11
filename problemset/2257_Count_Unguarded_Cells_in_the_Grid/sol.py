from typing import List

def inside(x, y, m, n):
    return x >= 0 and x < m and y >= 0 and y < n

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
                
        matrix = [[0] * n for _ in range(m)] 
        
        for g in guards:
            matrix[g[0]][g[1]] = -1
        for w in walls:
            matrix[w[0]][w[1]] = -1
        
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for g in guards:            
            for d in directions:
                x, y = g[0], g[1]
                while inside(x + d[0], y + d[1], m, n) and matrix[x + d[0]][y + d[1]] != -1:
                    x, y = x + d[0], y + d[1]
                    matrix[x][y] = 1
        count = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    count += 1

        
        return count        