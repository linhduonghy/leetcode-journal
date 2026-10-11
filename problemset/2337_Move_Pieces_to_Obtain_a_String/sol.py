class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        n = len(start)
        
        lpos1 = [i for i in range(n) if start[i] == 'L' ]
        lpos2 = [i for i in range(n) if target[i] == 'L' ]
                
        rpos1 = [i for i in range(n) if start[i] == 'R' ]
        rpos2 = [i for i in range(n) if target[i] == 'R' ]
        
        if len(lpos1) != len(lpos2) or len(rpos1) != len(rpos2):
            return False
        
        acc_rpos1 = [0] * n
        if start[0] == 'R':
            acc_rpos1[0] = 1
        for i in range(n - 1):
            acc_rpos1[i + 1] = acc_rpos1[i]
            if start[i + 1] == 'R':
                acc_rpos1[i + 1] += 1
        
        acc_lpos1 = [0] * n
        if target[-1] == 'L':
            acc_lpos1[-1] = 1
        for i in range(n - 1, 0, -1):
            acc_lpos1[i - 1] = acc_lpos1[i]
            if target[i - 1] == 'L':
                acc_lpos1[i - 1] += 1
                
        
        def containR(fr: int, to: int) -> bool:
            t = acc_rpos1[to]
            if fr > 0:
                t -= acc_rpos1[fr - 1]
            return t > 0
        
        def containL(fr: int, to: int) -> bool:
            t = acc_lpos1[fr]
            if to < n - 1:
                t -= acc_lpos1[to + 1]
            return t > 0
         
        # check move left   
        j = 0
        for i in range(len(lpos1)):
            # can't move right
            if lpos1[i] < lpos2[j]:
                return False
            # have 'R' between start 'L' and target 'R' => can't move left
            if containR(lpos2[j], lpos1[i]):
               return False 
            j += 1
        
        # check move right
        j = len(rpos1) - 1
        for i in range(len(rpos1) - 1, -1, -1):
            if rpos1[i] > rpos2[j]:
                return False
            if containL(rpos1[i], rpos2[j]):
                return False
            j -= 1
        
        return True
            
        
        