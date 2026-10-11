from typing import List
import re
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        wordCount1 = Counter(re.split(r'\s+', s1))
        wordCount2 = Counter(re.split(r'\s+', s2))
        
        res = []
        for k, v in wordCount1.items():
            if v == 1 and k not in wordCount2:
               res.append(k)
        
        for k, v in wordCount2.items():
            if v == 1 and k not in wordCount1:
               res.append(k)
                
        return res