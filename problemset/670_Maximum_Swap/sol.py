class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        for i in range(len(s) - 1):
            maxV = s[i]
            maxI = -1
            for j in range(len(s) - 1, i, -1):
                if s[j] > maxV:
                    maxV = s[j]
                    maxI = j
            if maxI != -1:
                s[i], s[maxI] = s[maxI], s[i]
                break
        
        return int("".join(s))            
