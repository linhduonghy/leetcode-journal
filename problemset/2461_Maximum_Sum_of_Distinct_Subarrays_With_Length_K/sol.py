from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        frequent = {}
        
        sum = 0
        for i in range(k):
            sum += nums[i]
            if nums[i] not in frequent:
                frequent[nums[i]] = 1
            else:
                frequent[nums[i]] += 1
            
        res = 0
        if len(frequent) == k:
            res = sum
        for i in range(k, len(nums)):
            sum = sum + nums[i] - nums[i - k]
            if nums[i] not in frequent:
                frequent[nums[i]] = 1
            else:
                frequent[nums[i]] += 1
            
            tmp = frequent[nums[i - k]]
            if tmp == 1:
                frequent.pop(nums[i - k])
            else:
                frequent[nums[i - k]] = tmp - 1
                               
            if len(frequent) == k:
                res = max(res, sum)
        
        return res