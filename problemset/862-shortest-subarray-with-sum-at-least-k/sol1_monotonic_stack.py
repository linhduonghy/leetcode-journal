from typing import List, Tuple

def find_candidate_index(sum_stack: List[Tuple[int, int]], target: int):
    low, high = 0, len(sum_stack) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if sum_stack[mid][0] <= target:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1
    return ans


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        cumulative_sum = 0
        monotonic_stack = []
        ans = len(nums) + 1
        for i, num in enumerate(nums):
            cumulative_sum += num
            if cumulative_sum >= k:
                ans = min(ans, i + 1)
            while monotonic_stack and monotonic_stack[-1][0] >= cumulative_sum:
                monotonic_stack.pop()

            monotonic_stack.append((cumulative_sum, 1))

            candidate_index = find_candidate_index(monotonic_stack, cumulative_sum - k)

            if candidate_index != -1:
                ans = min(ans, i - monotonic_stack[candidate_index][1])

        return -1 if ans == (len(nums) + 1) else ans

