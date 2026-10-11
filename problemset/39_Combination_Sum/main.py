class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        
        result = []
        self.backtrack(candidates, target, 0, [], 0, result)
        return result
        
    def backtrack(self, candidates: List[int], target: int, index: int, cur: List[int], sum: int, result: List[List[int]]):
        if (sum > target):
            return
        if (sum == target):
            result.append(list(cur))
            return
        
        for i in range(index, len(candidates)):
            cur.append(candidates[i])
            self.backtrack(candidates, target, i, cur, sum + candidates[i], result)
            cur.pop()
            
        