from heapq import heappop, heappush


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        uglyHeap = [1]
        visited = set()
        visited.add(1)
        primes = [2, 3, 5]
        cnt = 1
        while cnt < n:
            cur = heappop(uglyHeap)
            for p in primes:
                if cur * p not in visited:
                    heappush(uglyHeap, cur * p)
                    visited.add(cur * p)
            cnt += 1
        return heappop(uglyHeap)

if __name__ == "__main__":
    print(Solution().nthUglyNumber(20))