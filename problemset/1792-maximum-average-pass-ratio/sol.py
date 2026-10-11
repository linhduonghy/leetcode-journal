import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def _gain_pass_ratio(passed: int, total: int):
            return (passed + 1) / (total + 1) - passed / total

        pass_ratios = []

        for cls in classes:
            heapq.heappush(pass_ratios, (-_gain_pass_ratio(cls[0], cls[1]), cls[0], cls[1]))

        while extraStudents > 0:
            _, passes, totals = heapq.heappop(pass_ratios)
            heapq.heappush(pass_ratios, (-_gain_pass_ratio(passes + 1, totals + 1), passes + 1, totals + 1))
            extraStudents -= 1

        ans = 0
        for _, passes, totals in pass_ratios:
            ans += passes / totals

        return ans / len(classes)