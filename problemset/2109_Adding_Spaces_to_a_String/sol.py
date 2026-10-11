from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        res = []
        cur_spaces = 0
        n = len(spaces)
        for i in range(len(s)):
            if cur_spaces < n and i == spaces[cur_spaces]:
                res.append(" ")
                cur_spaces += 1
            res.append(s[i])    
        
        return "".join(res)