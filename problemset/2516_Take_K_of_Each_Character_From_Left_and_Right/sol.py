
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        if k == 0:
            return 0
        n = len(s)
        frequent = [[0] * 3 for _ in range(n)]  

        frequent[0][ord(s[0]) - ord('a')] = 1
        for i in range(1, n):
            for j in range(3):
                frequent[i][j] = frequent[i - 1][j]
            frequent[i][ord(s[i]) - ord('a')] += 1
        def count(l: int, r: int, c: int):
            if l == -1 or l > r or r >= n:
                return 0
            if l == 0:
                return frequent[r][c]
            return frequent[r][c] - frequent[l - 1][c]
        
        i = -1
        j = 0
        res = n + 1
        while i < n:
            count_left = [count(0, i, o) for o in range(3)]
            while j <= n:
                count_right = [count(j, n - 1, o) for o in range(3)]
                can_next = True
                for o in range(3):
                    if count_left[o] + count_right[o] < k:
                        can_next = False
                        break
                if can_next:
                    res = min(res, i + 1 + (n - 1) - j + 1)
                    j += 1
                else:
                    break
            i += 1
        return -1 if res == (n + 1) else res