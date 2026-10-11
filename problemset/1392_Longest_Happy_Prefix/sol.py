class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        pi = [0] * n
        for i in range(1, n):
            j = pi[i - 1]
            while j > 0 and s[i] != s[j]:
                j = pi[j - 1]
            if s[i] == s[j]:
                pi[i] = j + 1
        return s[:pi[n - 1]]
    
print(Solution().longestPrefix("abcdefbcdefabcdef"))