import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, 'a'))
        if b > 0:
            heapq.heappush(pq, (-b, 'b'))
        if c > 0:
            heapq.heappush(pq, (-c, 'c'))

        result = []

        while pq:
            cnt, char = heapq.heappop(pq)
            if len(result) >= 2 and result[-1] == char and result[-2] == char: # contain three character continuously
                if not pq:
                    break
                cnt1, char1 = heapq.heappop(pq) # get second frequent character
                result.append(char1)
                cnt1 = -cnt1 - 1
                if cnt1 > 0:
                    heapq.heappush(pq, (-cnt1, char1))
                heapq.heappush(pq, (cnt, char))

            else:
                result.append(char)
                cnt = -cnt - 1
                if cnt > 0:
                    heapq.heappush(pq, (-cnt, char))
        return "".join(result)