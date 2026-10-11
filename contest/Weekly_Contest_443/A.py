from typing import List

class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:

        result = [cost[0]]
        mi = cost[0]
        for i in range(1, len(cost)):
            if cost[i] <= mi:
                mi = cost[i]
                result.append(cost[i])
            else:
                result.append(mi)

        return result