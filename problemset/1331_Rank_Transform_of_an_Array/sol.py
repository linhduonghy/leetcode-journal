    from typing import List

    class Solution:
        def arrayRankTransform(self, arr: List[int]) -> List[int]:
            
            n = len(arr)

            if n == 0:
                return []
                
            arr = [(i, arr[i]) for i in range(n)]
            arr.sort(key= lambda x : x[1])
            
            res = [0] * n
            res[arr[0][0]] = 1
            cnt = 1
            for i in range(1, n):
                if arr[i][1] != arr[i - 1][1]:
                    cnt += 1
                res[arr[i][0]] = cnt
                        
            return res