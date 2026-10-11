class Solution:
    def getLucky(self, s: str, k: int) -> int:

        def transform(s: str) -> int:
            return sum([(ord(c) - ord('0')) for c in s])
        s = ''.join([str(ord(c) - ord('a') + 1) for c in s])
        while k > 0:
            ss = transform(s)
            s = str(ss)
            k -= 1

        return int(s)