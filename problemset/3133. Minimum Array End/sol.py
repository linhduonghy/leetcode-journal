class Solution:
    def minEnd(self, n: int, x: int) -> int:

        res = x
        while n > 1:

            res = (res + 1) | x
            n -= 1

        return res
