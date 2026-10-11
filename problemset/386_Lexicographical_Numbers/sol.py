from typing import List

def generate(cur: int, n: int, res: List[int]):
    if cur > n:
        return
    res.append(cur)
    for i in range(10):
        generate(cur * 10 + i, n, res)

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        res = []
        for i in range(1, 10):
            generate(i, n, res)

        return res