from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        for i in range(k - 1):
            colors.append(colors[i])

        n = len(colors)

        group_len = 1
        ans = 0
        for i in range(1, n):
            if colors[i] == colors[i-1]:
                group_len = 1
                continue

            group_len += 1
            if group_len >= k:
                ans += 1

        return ans


