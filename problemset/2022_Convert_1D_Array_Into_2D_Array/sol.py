from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if m * n != len(original):
            return []

        res = []
        for i in range(m):
            res.append(original[i * n : (i + 1) * n])

        return res

if __name__ == '__main__':
    Solution().construct2DArray([1,1,1,1], 4, 1)

