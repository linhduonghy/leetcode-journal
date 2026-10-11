class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:

        cnt = [0] * 26

        for i in range(len(s)):
            cnt[ord(s[i]) - 97] += 1

        for _ in range(t):
            cnt_z = cnt[25]
            for i in range(24, -1, -1):
                cnt[i + 1] = cnt[i]
            if cnt_z > 0:
                cnt[0] = cnt_z
                cnt[1] = (cnt[1] + cnt_z) % 1000000007
            else:
                cnt[0] = 0

        res = 0
        for i in range(26):
            res = (res + cnt[i]) % 1000000007

        return res