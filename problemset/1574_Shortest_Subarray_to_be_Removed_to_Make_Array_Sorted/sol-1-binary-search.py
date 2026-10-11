from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        incLeft = [False] * n
        incRight = [False] * n
        
        incLeft[0] = True
        ans = n
        for i in range(1, n):
            if arr[i - 1] > arr[i]:                
                ans = min(ans, n - i)                
                break
            incLeft[i] = True
        
        if incLeft[-1]:
            return 0
        
        incRight[-1] = True
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                ans = min(ans, i + 1)
                break
            incRight[i] = True
        
        def can_remove_sub(size: int):
            for i in range(0, n - size - 1):
                if arr[i] <= arr[i + size + 1] and incLeft[i] and incRight[i + size + 1]:
                    return True
            return False
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            if can_remove_sub(mid):
               ans = min(mid, ans)
               r = mid - 1
            else:
                l = mid + 1
        
        return ans
        
        
if __name__ == "__main__":
    Solution().findLengthOfShortestSubarray([2,2,2,1,1,1])