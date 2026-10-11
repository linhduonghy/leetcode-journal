
def max_length_palindrome(s: str):

    max_length_from_index = [1] * len(s)
    max_length_from_index[-1] = 0
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if left > 0:
                max_length_from_index[left - 1] = max(max_length_from_index[left - 1], right - left + 1)
            left -= 1
            right += 1
        return right - left - 1  # Length of palindrome

    max_length = 0
    for i in range(len(s)):
        max_length = max(max_length, expand_around_center(i, i))      # Odd length palindrome
        max_length = max(max_length, expand_around_center(i, i + 1))  # Even length palindrome

    return max_length, max_length_from_index

class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:

        t = t[::-1]
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        max_length_s, max_length_from_index_s = max_length_palindrome(s)
        max_length_t, max_length_from_index_t = max_length_palindrome(t)
        res = max(max_length_s, max_length_t)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j] * 2 + max(max_length_from_index_s[i - 1], max_length_from_index_t[j - 1]))
                else:
                    dp[i][j] = 0

        return res


if __name__ == '__main__':
    Solution().longestPalindrome("abcde", "ecdba")