class Solution:
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        self.genPermute(nums, 0, result)
        return result
    def genPermute(self, nums: List[int], l: int, result: []):
        if l == len(nums) - 1:
            result.append(nums[0:])
            return
        map = {}
        for i in range(l, len(nums)):
            num = nums[i]
            if num not in map:
                nums[i], nums[l] = nums[l], nums[i]
                self.genPermute(nums, l + 1, result)
                nums[i], nums[l] = nums[l], nums[i]
                map[num] = True
                
    
    
    
        