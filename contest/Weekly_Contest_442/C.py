from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:

        n, m = len(skill), len(mana)

        prev = [0] * n
        prev[0] = skill[0] * mana[0]
        for i in range(1, n):
            prev[i] = prev[i - 1] + skill[i] * mana[0]
        # print(prev)
        for i in range(1, m):
            cur = [0] * n
            cur[0] = prev[0] + skill[0] * mana[i]
            for j in range(1, n):
                if prev[j] > cur[j - 1]:
                    cur[j] = prev[j] + skill[j] * mana[i]
                else:
                    cur[j] = cur[j - 1] + skill[j] * mana[i]
            for j in range(n - 2, -1, -1):
                cur[j] = cur[j + 1] - skill[j + 1] * mana[i]
            # print(cur)
            prev = cur

        return prev[-1]

