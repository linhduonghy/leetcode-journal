from typing import List

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:

        n = len(grid)
        m = len(grid[0])
        for row in grid:
            row.sort(reverse=True)

        cur_pos = [0] * n
        res = 0
        set_row = []
        for i in range(n):
            if cur_pos[i] < m and cur_pos[i] < limits[i]:
                set_row.append(i)
        set_row = set(set_row)

        while k > 0:
            max_val = -1
            max_pos = -1
            for i in set_row:
                if max_val <= grid[i][cur_pos[i]]:
                    max_val = grid[i][cur_pos[i]]
                    max_pos = i
            if max_pos == -1:
                break
            res += max_val
            cur_pos[max_pos] += 1
            k -= 1
            if cur_pos[max_pos] >= m or cur_pos[max_pos] >= limits[max_pos]:
                set_row.remove(max_pos)
        return res

if __name__ == '__main__':
    s = Solution()
    s.maxSum([[15],[1],[41],[30]], [0,0,1,1], 2)