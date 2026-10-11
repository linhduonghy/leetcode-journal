class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        s = needle + "#" + haystack
        n = len(s)
        pi = [0] * n
        for i in range(1, n):
            j = pi[i - 1]
            while j > 0 and s[i] != s[j]:
                j = pi[j - 1]
            if s[i] == s[j]:
                pi[i] = j + 1            
            if pi[i] == m:
                return i - 2 * m
        return -1