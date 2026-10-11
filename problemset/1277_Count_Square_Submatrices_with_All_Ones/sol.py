
from typing import List




class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        res = 0
        m = len(matrix)
        n = len(matrix[0])

        count = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                count[i][j] = count[i - 1][j] + count[i][j - 1] - count[i - 1][j - 1] + matrix[i - 1][j - 1]

        def cal_count(sx: int, sy: int, ex: int, ey: int):
            return count[ex][ey] - count[ex][sy - 1] - count[sx - 1][ey] + count[sx - 1][sy - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(1, min(m  + 1 - i, n + 1 - j) + 1):
                    c = cal_count(i, j, i + k - 1, j + k - 1)
                    if k ** 2 == c:
                        res += 1
        return res

if __name__ == '__main__':
    Solution().countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]])