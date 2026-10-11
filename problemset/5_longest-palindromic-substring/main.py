class Solution:

    def longestPalindrome(self, s: str) -> str:
        x = self.findLongestPalindrome(s, 0)
        x = max(self.findLongestPalindrome(s, 1), x)

        for l in range(0, len(s)):
            r = l + x
            if r == len(s) + 1:
                break
            ss = s[l:r]
            if (self.checkPalindrome(ss)):
                return ss
        return s[0]

    def findLongestPalindrome(self, s: str, k: int) -> int:
        x = k
        d = [x + i for i in range(0, len(s) + 1, 2) if x + i <= len(s)]
        l, r = 0, len(d) - 1
        ans = 0
        print('d ', d)
        while l <= r:
            mid = (l + r) // 2
            print('len ', d[mid])
            if self.checkLengthPalindrome(s, d[mid]):
                l = mid + 1
                ans = max(ans, d[mid])
            else:
                r = mid - 1
        return ans

    def checkLengthPalindrome(self, s, x):
        for l in range(0, len(s)):
            r = l + x
            if r == len(s) + 1:
                break
            ss = s[l:r]
            print(ss)
            if (self.checkPalindrome(ss)):
                return True
        return False

    def checkPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while (l < r ):
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


s = Solution()
print(s.longestPalindrome("bbbb"))
