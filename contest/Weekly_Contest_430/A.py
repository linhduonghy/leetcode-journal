from typing import List
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:

        answer = 0
        for i in range(len(grid[0])):
            for j in range(1, len(grid)):
                if grid[j][i] <= grid[j-1][i]:
                    answer += grid[j-1][i] - grid[j][i] + 1
                    grid[j][i] = grid[j - 1][i] + 1

        return answer
