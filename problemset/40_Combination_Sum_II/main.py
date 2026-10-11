class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        print(candidates)
        result = []
        self.backtrack(candidates, target, 0, 0, [], result)
        return result

    def backtrack(self, candidates: List[int], target, index: int, curSum: int, curEle: List[int], result: []):
        if index >= len(candidates) or curSum > target:            
            if target == curSum:
                result.append(list(curEle))
            return
        if target == curSum:
            result.append(list(curEle))
            return
        
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            curEle.append(candidates[i])
            self.backtrack(candidates, target, i + 1, curSum + candidates[i], curEle, result)
            curEle.pop()