class Solution:

    """ 
        Dynamic Programming Approach

        P[i][j] = true  substring (i, j) is palindrome
                = false otherwise
        
        P[i][j] = P[i + 1][j - 1] and S[i] = S[j]

    """
    def longestPalindrome(self, s: str) -> str:
        
        P = [[True] * len(s) for i in range(len(s))]
     
        for i in range(len(s) - 1):
            P[i][i + 1] = s[i] == s[i + 1]

        max_length = 0
        l, r = 0, 0
        for i in range(len(s) - 2, -1, -1):
            for j in range(i, len(s)):
                P[i][j] = P[i + 1][j - 1] and s[i] == s[j]
                if P[i][j] and (max_length < j - i + 1):
                    max_length = j - i + 1
                    l = i
                    r = j
        return s[l: r + 1]
        
# s = Solution()
# s.longestPalindrome('cbbd')