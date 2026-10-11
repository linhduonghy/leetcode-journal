from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        prefix_max = arr[:]
        suffix_min = arr[:]

        n = len(arr)
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], arr[i])

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], arr[i])

        chunks = 1
        for i in range(1, n):
            if prefix_max[i - 1] < suffix_min[i]:
                chunks += 1
        return chunks
