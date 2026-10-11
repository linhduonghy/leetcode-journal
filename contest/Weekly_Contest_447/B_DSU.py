from typing import List

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n

    def find(self, x):
        if x == self.p[x]:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.r[x] < self.r[y]:
            self.p[x] = self.p[y]
        else:
            self.p[y] = self.p[x]
            if self.r[x] == self.r[y]:
                self.r[x] += 1

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] <= maxDiff:
                dsu.union(i, i + 1)
        result = []
        for query in queries:
            result.append(dsu.find(query[0]) == dsu.find(query[1]))
        return result
