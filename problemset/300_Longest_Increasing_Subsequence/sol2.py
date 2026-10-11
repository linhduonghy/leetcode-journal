class Solution:
    """
        Sol O(nlogn)
        
        h[i]: Giá trị kết thúc nhỏ nhất của dãy con tăng độ dài i
        h[i] < h[i + 1] -> binary search
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        h = [10001] * len(nums)
        h[0] = nums[0]
        for i in range(1, len(nums)):            
            # print(i, nums[i])
            # print(dp)
            # print(h)
            index = self.find(h, 0, len(nums) - 1, nums[i])
            # print(index)
            if index == -1:
                h[0] = min(h[0], nums[i])
                
            else:
                dp[i] = index + 1
                h[dp[i]] = min(h[dp[i]], nums[i])
            
        return max(dp) + 1
    
    def find(self, h: List[int], l: int, r: int, target: int) -> int:
        result = -1
        while l <= r:
            mid = (l + r) >> 1
            if h[mid] < target:
                l = mid + 1
                result = mid
            else:
                r = mid - 1
        return result

            

