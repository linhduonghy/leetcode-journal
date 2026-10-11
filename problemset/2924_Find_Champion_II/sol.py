from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        in_degree = [0] * n
        
        for edge in edges:
            in_degree[edge[1]] += 1
        
        count_degree_0 = 0
        vertex_degree_0 = -1
        for i in range(n):
            
            if in_degree[i] == 0:
                if count_degree_0 == 1:
                    return -1
                count_degree_0 += 1
                vertex_degree_0 = i
        
        return vertex_degree_0
                    
            