from typing import List


def almostEqual(x, y):

    if x == y:
        return 1
    x = str(x)
    y = str(y)

    while len(x) < len(y): x = '0' + x
    while len(y) < len(x): y = '0' + y

    numDiff = []

    for i in range(len(x)):
        if x[i] != y[i]:
            numDiff.append(i)

    if len(numDiff) != 2:
        return 0

    if x[numDiff[0]] == y[numDiff[1]] and x[numDiff[1]] == y[numDiff[0]]:
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
    print(s.countPairs([123,231]))

