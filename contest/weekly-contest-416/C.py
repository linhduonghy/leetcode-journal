class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:

        arr1 = [ord(c) - ord('a') for c in word1]
        arr2 = [ord(c) - ord('a') for c in word2]

        cnt1 = [[0 for _ in range(26)] for _ in range(len(arr1))]
        cnt2 = [0 for _ in range(26)]

        for x in arr2:
            cnt2[x] += 1

        n = len(arr1)
        m = len(arr2)

        cnt1[0][arr1[0]] = 1
        for i in range(1, n):
            for c in range(26):
                cnt1[i][c] = cnt1[i - 1][c]
                if arr1[i] == c:
                    cnt1[i][c] += 1

        def canRearrange(i: int, j: int):
            for c in range(26):
                k = cnt1[j][c] if i == 0 else cnt1[j][c] - cnt1[i - 1][c]
                if k < cnt2[c]:
                    return False
            return True

        res = 0
        for i in range(0, n - m + 1):
            l = i
            r = n - 1
            minJ = n + 1
            while l <= r:
                j = (l + r) // 2
                if canRearrange(i, j):
                    minJ = min(minJ, j)
                    r = j - 1
                else:
                    l = j + 1
            if minJ != (n + 1):
                res += (n - 1 - minJ + 1)
        return res

if __name__ == '__main__':
    Solution().validSubstringCount("bbbb", "b")