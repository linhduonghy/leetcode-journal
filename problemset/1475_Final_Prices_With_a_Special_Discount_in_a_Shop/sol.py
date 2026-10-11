from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        stack = []
        ans = []

        for i in range(len(prices) - 1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            if not stack:
                ans.append(prices[i])
            else:
                ans.append(prices[i] - stack[-1])

            stack.append(prices[i])
        return ans