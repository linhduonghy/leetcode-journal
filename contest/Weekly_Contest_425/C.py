import math
from heapq import heappush, heappop
from typing import List


class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:

        pq = []
        for num in nums:
            heappush(pq, (-num, 0, 0))

        ans = 0
        while pq and (op1 > 0 or op2 > 0):
            top = heappop(pq)
            v = -top[0]
            print(v, '----', top)
            if v == 0:
                break
            if top[1] == 1 and top[2] == 1:
                ans += v
                continue
            if op1 > 0 and op2 > 0 and top[1] == 0 and top[2] == 0 and v >= k:
                v1 = math.ceil(v / 2)
                v2 = v - k
                if v2 <= v1:
                    print('op2')
                    op2 -= 1
                    heappush(pq, (-v2, top[1], 1))
                else:
                    print('op1')
                    op1 -= 1
                    heappush(pq, (-v1, 1, top[2]))
            elif op1 > 0 and top[1] == 0:
                print('op1')
                heappush(pq, (-math.ceil(v / 2), 1, top[2]))
                op1 -= 1
            elif op2 > 0 and top[2] == 0 and v >= k:
                print('op2')
                heappush(pq, (-(v - k), top[1], 1))
                op2 -= 1
            print('after', pq)
        print(ans)
        return ans - sum([t[0] for t in pq])


if __name__ == '__main__':
    print(Solution().minArraySum([2,4,3], 3, 2, 1))
