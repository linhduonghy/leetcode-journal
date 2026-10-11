from typing import List
class Solution:
    def stringSequence(self, target: str) -> List[str]:

        cur = target[0]
        res = [chr(i) for i in range(ord('a'), ord(cur[0]) + 1)]
        len = 1
        target = target[1:]
        for c in target:
            for i in range(ord('a'), ord(c) + 1):
                cur = cur[:len] + chr(i)
                res.append(cur)
            len += 1
        return res
if __name__ == '__main__':
    S = Solution().stringSequence("abc")