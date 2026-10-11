class Solution:
    def minimumSteps(self, s: str) -> int:
        
        cnt1 = 0
        res = 0
        for c in s:
            if c == '1':
                cnt1 += 1
            else:
                res += cnt1
            
        return res