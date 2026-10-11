from cProfile import runctx


def atLeastOne(cnt: list):
    return cnt[0] > 0 and cnt[1] > 0 and cnt[2] > 0

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = [0] * 3
        n = len(s)
        left, right = 0, 0
        ans = 0
        while left < n:
            while right < n and not atLeastOne(cnt):
                cnt[ord(s[right]) - 97] += 1
                right += 1
            if atLeastOne(cnt):
                ans += n - right
            cnt[ord(s[left]) - 97] -= 1
            left += 1
        return ans


