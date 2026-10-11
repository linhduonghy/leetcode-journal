from typing import List

def calNextCost(nextCost: List[int], l: int, r: int) -> int:
    c = 0
    if l < r:
        for i in range(l, r):
            c += nextCost[i]
        return c

    for i in range(l, len(nextCost)):
        c += nextCost[i]
    for i in range(r):
        c += nextCost[i]
    return c

def calPrevCost(previousCost: List[int], l: int, r: int) -> int:
    c = 0
    if r < l:
        for i in range(r + 1, l + 1):
            c += previousCost[i]
        return c
    for i in range(0, l + 1):
        c += previousCost[i]
    for i in range(r + 1, len(previousCost)):
        c += previousCost[i]
    return c


class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:

        res = 0
        for i in range(len(s)):
            fr = ord(s[i]) - ord('a')
            to = ord(t[i]) - ord('a')
            if fr == to:
                continue
            res += min(calNextCost(nextCost, fr, to), calPrevCost(previousCost, fr, to))
        return res

if __name__ == '__main__':
    Solution().shiftDistance("ccdbbcaadb", "aadbbdaaac",
                  [6,6,9,8,2,4,10,10,6,4,9,5,5,5,2,7,9,7,4,1,4,10,1,5,2,4], [0,4,5,6,7,10,5,5,8,1,1,10,7,8,10,8,7,2,3,3,6,3,0,6,4,0])