from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        allow_character = [0 for c in range(0, ord('z') + 1)]
        
        for c in allowed:
            allow_character[ord(c)] = 1
        
        res = 0
        
        for word in words:
            isAllowed = 1
            for c in word:
                if allow_character[ord(c)] == 0: 
                    isAllowed = 0
                    break
            res += isAllowed
    
        return res
            
        
                