class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 1
        s = 4
        for _ in range(n - 1):
            ans += s
            s += 4
        return ans