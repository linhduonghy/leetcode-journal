class Solution:

    # s + '#' + t
    # only store prefix function of beginning 

    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        pi = [0] * m
        for i in range(1, m):
            j = pi[i - 1]
            while j > 0 and needle[i] != needle[j]:
                j = pi[j - 1]
            if needle[i] == needle[j]:
                pi[i] = j + 1

        pc = 0
        n = len(haystack)
        for i in range(0, n):
            j = pc
            while j > 0 and haystack[i] != needle[j]:
                j = pi[j - 1]
            pc = j + 1 if haystack[i] == needle[j] else 0
            if pc == m:
                return i - m + 1
        return -1

print(Solution().strStr("sasdbsadutsad", "sad"))