from typing import List

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        
        n = len(s)
        cnt0 = [[0 for i in range(n)] for j in range(n)]
        cnt1 = [[0 for i in range(n)] for j in range(n)]
        
        for i in range(0, n):
            if s[i] == '0':
                cnt0[i][i] = 1
            else:
                cnt1[i][i] = 1
            
        for i in range(n - 1):
            for j in range(i + 1, n):
                cnt0[i][j] = cnt0[i][j - 1]
                cnt1[i][j] = cnt1[i][j - 1]
                if s[j] == '0':
                    cnt0[i][j] += 1
                else:
                    cnt1[i][j] += 1
        
        res = 0
        for i in range(n):
            for j in range(i, n):
                print(i, j, cnt0[i][j], cnt1[i][j])
                if cnt0[i][j] <= k or cnt1[i][j] <= k :
                    res += 1
        return res
        
if __name__ == "__main__":
    
    s = Solution()
    print(s.countKConstraintSubstrings("11111", 1))