class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        cnt = 0
        res = 0
        for c in s:
            cnt += 1 if c == '(' else -1
            if cnt < 0:
                res += 1
                cnt += 1
        return res + cnt

