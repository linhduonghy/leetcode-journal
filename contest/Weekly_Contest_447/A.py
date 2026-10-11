from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        maxX = [-1 for _ in range(n + 1)]
        maxY = [-1 for _ in range(n + 1)]
        minX = [float('inf') for _ in range(n + 1)]
        minY = [float('inf') for _ in range(n + 1)]
        for building in buildings:
            maxX[building[0]] = max(maxX[building[0]], building[1])
            minX[building[0]] = min(minX[building[0]], building[1])
            maxY[building[1]] = max(maxY[building[1]], building[0])
            minY[building[1]] = min(minY[building[1]], building[0])

        ans = 0
        for building in buildings:
            x, y = building[0], building[1]
            if minY[y] < x < maxY[y] and minX[x] < y < maxX[x]:
                ans += 1
        return ans
