from typing import List 

def buildPrefixOcc(prefixOccurrence: set, x: int):
    
    s = str(x)
    for i in range(len(s)):
        prefixOccurrence.add(s[:i + 1])
    
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        prefixOccurrence = set()
        
        for x in arr1:
            buildPrefixOcc(prefixOccurrence, x)
        
        res = 0
        for x in arr2:
            s = str(x)
            for i in range(len(s)):
                if s[: i + 1] in prefixOccurrence:
                    res = max(res, i + 1)
        
        return res     