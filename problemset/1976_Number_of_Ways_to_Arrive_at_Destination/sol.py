from typing import List
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        adj = [[] * n for _ in range(n)]
        for road in roads:
            adj[road[0]].append((road[1], road[2]))
            adj[road[1]].append((road[0], road[2]))
        mod = 10**9 + 7
        pq = []
        dp = [[float("inf"), 0] for _ in range(n)]
        dp[0][1] = 1
        heapq.heappush(pq, (0, 0))
        while pq:
            cur_time, source = heapq.heappop(pq)
            # print(cur_time, source)
            for dest, time  in adj[source]:
                # print(dest, time, dp[dest])
                if dp[dest][0] > cur_time + time:
                    dp[dest][0] = cur_time + time
                    dp[dest][1] = dp[source][1]
                    heapq.heappush(pq, (dp[dest][0], dest))
                elif dp[dest][0] == cur_time + time:
                    dp[dest][1] = (dp[dest][1] + dp[source][1]) % mod
        
        return dp[n-1][1]
        
                
        