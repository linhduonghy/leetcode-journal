'''
    find number of elements between two prefix x and y
'''
def countElementsBetween(x: int, y: int, n: int) -> int:
    eles = 0
    while x <= n:
        eles += min(y, n + 1) - x
        x *= 10
        y *= 10
    return eles


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        prefixCurrent = 1
        k -= 1
        while k > 0:
            numberOfElementsBetween = countElementsBetween(prefixCurrent, prefixCurrent + 1, n)
            print(prefixCurrent, numberOfElementsBetween)
            if numberOfElementsBetween <= k:
                prefixCurrent += 1 # go to next sibling
                k -= numberOfElementsBetween
            else:
                prefixCurrent *= 10 # go to subtree of prefix
                k -= 1
        return prefixCurrent

