import heapq
from typing import List


class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:

        res = []

        if len(queries) < k:
            return [-1 for i in range(len(queries))]

        def distance(point: List[int]):
            return abs(point[0]) + abs(point[1])

        h = []
        for i in range(0, k - 1):
            res.append(-1)
            h.append(-distance(queries[i]))

        h.append(-distance(queries[k - 1]))
        heapq.heapify(h)
        maxV = heapq.heappop(h)
        res.append(-maxV)
        heapq.heappush(h, maxV)

        for i in range(k, len(queries)):
            query = queries[i]
            dis = distance(query)
            maxV = -heapq.heappop(h)
            if dis < maxV:
                heapq.heappush(h, -dis)
                maxV = -heapq.heappop(h)
            res.append(maxV)
            heapq.heappush(h, -maxV)

        return res


if __name__ == '__main__':
    print(Solution().resultsArray([[1, 2], [3, 4], [2, 3], [-3, 0]], 2))
