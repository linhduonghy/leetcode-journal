from typing import List

def xor(arr: list):
    r = 0
    for x in arr:
        r ^= x
    return r
class Solution:
    def __init__(self):
        self.ans = 0
        self.arr = []
        self.n = 0
    def subsetXORSum(self, nums: List[int]) -> int:
        self.n = len(nums)
        self.backtrack(0, nums)
        return self.ans
    def backtrack(self, i: int, nums: list ):
        if i == self.n:
            self.ans += xor(self.arr)
            return  
        self.arr.append(nums[i])
        self.backtrack(i + 1, nums)
        self.arr.pop()
        self.backtrack(i + 1, nums)