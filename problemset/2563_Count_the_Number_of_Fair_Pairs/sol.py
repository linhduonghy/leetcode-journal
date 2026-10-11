from typing import List

def findLeft(nums: List[int], minIndex: int, maxIndex: int, value):
    
    l = minIndex
    r = maxIndex
    res = maxIndex + 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] >= value:
            res = min(res, mid)
            r = mid - 1
        else:
            l = mid + 1
    return -1 if res == maxIndex + 1 else res
      
def findRight(nums: List[int], minIndex: int, maxIndex: int, value):
    
    l = minIndex
    r = maxIndex
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] <= value:
            res = max(res, mid)
            l = mid + 1
        else:
            r = mid - 1
    return res  

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()
        
        return self.countPair(nums, upper + 1) - self.countPair(nums, lower)
    
    def countPair(self, nums: List[int], value: int): 
        
        left = 0
        right = len(nums) - 1
        result = 0
        while left < right:
            sum = nums[left] + nums[right]
            if sum < value:
                result += right - left
                left += 1
            else:
                right -= 1
        return result