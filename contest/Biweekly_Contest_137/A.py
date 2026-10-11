from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == 1 or k == 1:
            return nums
        
        res = []
        n = len(nums)
        
        cnt = 0
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                cnt += 1
            else:
                cnt = 0
            
            if i + 1 >= k:
                if cnt + 1 >= k:
                    res.append(nums[i])
                else:
                    res.append(-1)
        
        return res
        
if __name__ == "__main__":
    
    s = Solution()
    s.resultsArray( [1, 1], 1)