class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
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
        
        curEle.append(candidates[index])
        self.backtrack(candidates, target, index + 1, curSum + candidates[index], curEle, result)
        curEle.pop()

        for i in range(index + 1, len(candidates)):
            if candidates[i] != candidates[index]:
                self.backtrack(candidates, target, i, curSum, curEle, result)
                break