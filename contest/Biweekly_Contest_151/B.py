from typing import List


class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:

        n = len(original)
        for i in range(1, n):
            diff = original[i] - original[i - 1]
            if bounds[i][0] - diff < bounds[i - 1][0]:
                bounds[i][0] = bounds[i - 1][0] + diff
            if bounds[i][1] - diff > bounds[i - 1][1]:
                bounds[i][1] = bounds[i - 1][1] + diff

        return 0 if bounds[-1][1] - bounds[-1][0] + 1 < 0 else bounds[-1][1] - bounds[-1][0] + 1

