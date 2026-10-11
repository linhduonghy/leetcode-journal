from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        s = mean * (len(rolls) + n)

        remain = s - sum(rolls)

        if remain / n > 6 or remain < n:
            return []
        
        ro = remain // n
        t1 = remain % n
        if t1 == 0:
            return [ro for _ in range(n)]
        t2 = t1 // (6 - ro)
        res = []
        for _ in range(t2):
            res.append(6)
        for _ in range(t2, n-1):
            res.append(ro)
        res.append(ro + (t1 % (6 - ro)))

        return res
