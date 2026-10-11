from collections import deque
from typing import List
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        moves = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

        def swap_indices(s, index1, index2):
            s_list = list(s)
            s_list[index1], s_list[index2] = s_list[index2], s_list[index1]
            return ''.join(s_list)

        target = "123450"
        start_state = "".join(str(num) for row in board for num in row)
        q = deque([start_state])
        visited = set()
        visited.add(start_state)
        cnt = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return cnt

                index_0 = cur.index("0")
                for index_ in moves[index_0]:
                    next_state = swap_indices(cur, index_0, index_)
                    q.append(next_state)
                    visited.add(next_state)
            cnt += 1
        return -1