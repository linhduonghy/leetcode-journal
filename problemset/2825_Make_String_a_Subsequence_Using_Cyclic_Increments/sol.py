
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        i2 = 0
        for i1 in range(len(str1)):
            if i2 < len(str2) and (str1[i1] == str2[i2] or (str1[i1] == 'z' and str2[i2] == 'a') or 
                                   ord(str1[i1] - 'a') + 1 == ord(str2[i2] - 'a')):
                i2 += 1
        
        return i2 == len(str2)            
                
        
        
        