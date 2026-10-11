'''
    aeioi -> 00000 ( 5 bits )

'''


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        res = 0

        charMap = [0] * 26
        charMap[ord('a') - ord('a')] = 1
        charMap[ord('e') - ord('a')] = 2
        charMap[ord('i') - ord('a')] = 4
        charMap[ord('o') - ord('a')] = 8
        charMap[ord('u') - ord('a')] = 16

        firstOccurrence = [-2] * 32
        firstOccurrence[0] = -1
        prefixXor = 0
        for i in range(len(s)):
            prefixXor ^= charMap[ord(s[i]) - ord('a')]
            prev = firstOccurrence[prefixXor]
            if prev == -2:
                firstOccurrence[prefixXor] = i
            else:
                res = max(res, i - prev)

        return res
