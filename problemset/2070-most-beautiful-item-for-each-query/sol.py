from typing import List

def bisect_right(x: int, items: List[List[int]], n: int):
    l = 0
    r = n - 1
    pos = -1
    while l <= r:
        mid = (l + r) // 2
        if items[mid][0] <= x:
            pos = max(pos, mid)
            l = mid + 1
        else:
            r = mid - 1
    return pos

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        answer = []

        items.sort(key=lambda x: x[0])

        n = len(items)
        max_beauty = [0] * n

        max_beauty[0] = items[0][1]
        for i in range(1, n):
            max_beauty[i] = max(max_beauty[i - 1], items[i][1])

        for query in queries:
            pos = bisect_right(query, items, n)
            if pos == -1:
                answer.append(0)
            else:
                answer.append(max_beauty[pos])
        return answer