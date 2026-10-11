from typing import List


def checkPair(x: str, y: str, x1: int, y1: int):
    return x[x1] == y[y1] and x[y1] == y[x1]


def almostEqual(x, y):
    if x == y:
        return 1

    x = str(x)
    y = str(y)

    while len(x) < len(y): x = '0' + x
    while len(y) < len(x): y = '0' + y

    digitsX = set()
    digitsY = set()
    for c in x:
        digitsX.add(ord(c) - ord('0'))
    for c in y:
        digitsY.add(ord(c) - ord('0'))

    if len(digitsX) != len(digitsY):
        return 0
    for c in digitsX:
        if c not in digitsY:
            return 0

    digitCountX = dict()
    digitCountY = dict()

    for digit in digitsX:
        digitCountX[digit] = 0
        digitCountY[digit] = 0

    n = len(x)
    for i in range(n):
        digitCountX[ord(x[i]) - ord('0')] += 1
        digitCountY[ord(y[i]) - ord('0')] += 1

    for digit in digitsX:
        if digitCountX[digit] != digitCountY[digit]:
            return 0

    numDiff = []
    for i in range(len(x)):
        if x[i] != y[i]:
            numDiff.append(i)

    if len(numDiff) > 4:
        return 0
    if len(numDiff) <= 3:
        return 1

    if (checkPair(x, y, numDiff[0], numDiff[1])
            or checkPair(x, y, numDiff[0], numDiff[2])
            or checkPair(x, y, numDiff[0], numDiff[3])):
        return 1
    return 0


class Solution:
    def countPairs(self, nums: List[int]) -> int:

        n = len(nums)
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                res += almostEqual(nums[i], nums[j])
        return res


if __name__ == "__main__":
    s = Solution()
