
class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        prev = [-1 for _ in range(128)]
        m = 0
        res = 0
        for i in range(n):
            c = ord(s[i])
            # print(m, i - m, prev[c], end=", ")
            if prev[c] >= (i - m):
                m = (i - prev[c])
            else:
                m += 1
            # print(m, i - m + )
            prev[c] = i
            res = res if res > m else m
        return res