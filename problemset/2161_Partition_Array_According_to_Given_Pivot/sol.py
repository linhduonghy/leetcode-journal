from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        smaller_arr = [num for num in nums if num < pivot]
        equal_arr = [num for num in nums if num == pivot]
        greater_arr = [num for num in nums if num > pivot]

        return smaller_arr + equal_arr + greater_arr
