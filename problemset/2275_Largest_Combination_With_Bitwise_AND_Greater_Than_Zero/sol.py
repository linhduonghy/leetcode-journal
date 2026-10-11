from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        
        cnt = [0] * 24
        for num in candidates:
            bin_str = '{0:24b}'.format(num)
            for i in range(24):
                if bin_str[i] == '1':
                    cnt[i] += 1
                    
        return max(cnt)
    
if __name__ == '__main__':
    
    print(Solution().largestCombination([16,17,71,62,12,24,14]))