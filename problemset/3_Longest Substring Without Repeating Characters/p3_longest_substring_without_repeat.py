import string

class Solution:
    """ using Binary Search
    """
    def __init__(self):
        """ prev1 : last position 
            prev2 : 2nd last position 
        """
        self.prev1 = []
        self.prev2 = []


    def checkSubStringWithoutRepeat(self, i, j):
        """ check in substring contains duplicate character
        """
        for c in range(128):
            # print(i, j, self.prev1[c], self.prev1[c])
            if self.prev1[c] != -1 and self.prev2[c] != -1 and self.prev2[c] >= i and self.prev1[c] <= j:
                return False
        return True

    def findLongestSubString(self, prev_length, i):
        """ - find min position x that substring(x, i) without repeat
            - if substring(x, i) True -> substring(x + 1, i) True
            -> binary search length of substring
        """
        l, r = 0, prev_length + 1
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if (self.checkSubStringWithoutRepeat(i - mid + 1, i)):
                l = mid + 1
                res = max(res, mid)
            else:
                r = mid - 1
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        self.prev1 = [-1 for _ in range(128)]
        self.prev2 = [-1 for _ in range(128)]
        result = 0
        prev_length = 0
        for i in range(n):
            self.prev2[ord(s[i])] = self.prev1[ord(s[i])]
            self.prev1[ord(s[i])] = i
            prev_length = self.findLongestSubString(prev_length, i)
            result = max(result, prev_length)
        return result