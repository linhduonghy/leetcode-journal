class Solution:
    def stringHash(self, s: str, k: int) -> str:

        n = len(s)
        result = ''
        for i in range(0, n, k):
            s1 = s[i : i + k]
            sum = 0
            for c in s1:
                sum += ord(c) - ord('a')
            result += chr((sum % 26) + ord('a'))
        return result

if __name__ == "__main__":
    
    s = Solution()
    s.stringHash( "abcd", 2)