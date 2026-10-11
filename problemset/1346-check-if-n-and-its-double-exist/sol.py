from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        exists = set()
        exists.add(arr[0])
        for i in range(1, len(arr)):
            if arr[i] * 2 in exists:
                return True
            if arr[i] % 2 == 0 and (arr[i] // 2) in exists:
                return True
            exists.add(arr[i])

        return False