from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        n = len(nums)
        special_subarr = []

        prev_index = 0
        nums.append(nums[-1])
        for i in range(1, n + 1):
            if (nums[i] + nums[i - 1]) % 2 == 1:
                continue
            if i - 1 > prev_index:
                special_subarr.append((prev_index, i - 1))
            prev_index = i
        
        pos = [-1] * n
        index_subarr = 0
        for i in range(n):
            if index_subarr < len(special_subarr) and i > special_subarr[index_subarr][1]:
                index_subarr += 1
            if index_subarr < len(special_subarr) and special_subarr[index_subarr][0] <= i and i <= special_subarr[index_subarr][1]:
                pos[i] = index_subarr                
        
        ans = []
        for query in queries:
            if query[0] == query[1]:
                ans.append(True)
                continue
            if pos[query[0]] != -1 and pos[query[1]] != -1 and pos[query[0]] == pos[query[1]]:
                ans.append(True)
            else:
                ans.append(False)                
        return ans
    
    
if __name__ == "__main__":
    Solution().isArraySpecial([4,3,1,6], [[0,2],[2,3]])