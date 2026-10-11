from typing import List 

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        ans = [0] * n
        for i in range(n):
            sign = 1
            if k < 0:
                sign = -1
            j = i
            cnt = 0
            s = 0
            while cnt < abs(k):
                cnt += 1
                j = j + sign
                if j == n:
                    j = 0
                if j == -1:
                    j = n - 1
                s += code[j]
            ans[i] = s        
        return ans
            