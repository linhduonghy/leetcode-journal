class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:

        freq_s = {}
        freq_t = {}
        size = len(s) // k
        for i in range(0, len(s), size):
            ss = s[i: i + size]
            st = t[i: i + size]
            if ss not in freq_s:
                freq_s[ss] = 0
            if st not in freq_t:
                freq_t[st] = 0
            freq_s[ss] += 1
            freq_t[st] += 1

        for ss in freq_s:
            if ss not in freq_t or freq_s[ss] != freq_t[ss]:
                return False
        return True