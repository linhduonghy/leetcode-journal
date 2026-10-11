
        
class Solution:

    def __init__(self) -> None:
        self.res = 0
        
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        cur_sub = [1] * n
        self.backtrack1(s, 1, n, cur_sub, 1)
        return self.res       
    
    def backtrack1(self, s: str, index: int, n: int, cur_sub: list, count: int):
        if index >= n:
            seen = set()
            cur = s[0]
            for i in range(1, n):
                if cur_sub[i] == cur_sub[i - 1]:
                    cur += s[i]
                else:
                    if cur in seen:
                        return
                    seen.add(cur)
                    cur = s[i]
                    
            if cur in seen:
                return
            seen.add(cur)
            self.res = max(self.res, count)
            return
        
        cur_sub[index] = count
        self.backtrack1(s, index + 1, n, cur_sub, count)            
        
        cur_sub[index] = count + 1
        self.backtrack1(s, index + 1, n, cur_sub, count + 1)            