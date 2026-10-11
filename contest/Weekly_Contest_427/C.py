from collections import deque
from typing import List

def cal_depth(adj: List[List[int]], n: int) -> List[List[int]]:
    count_depth = [[0] * n for _ in range(n)]
    for src in range(n):
        q = deque()
        visited = set()
        q.append((src, 0))
        visited.add(src)
        count_depth[src][0] = 1
        while q:
            u, depth = q.popleft()
            for v in adj[u]:
                if v not in visited:
                    count_depth[src][depth + 1] += 1
                    q.append((v, depth + 1))
                    visited.add(v)
    for src in range(n):
        for j in range(n - 1):
            if count_depth[src][j + 1] > 0:
                count_depth[src][j + 1] += count_depth[src][j]
            else:
                count_depth[src][j + 1] = count_depth[src][j]
    return count_depth


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:

        n, m = len(edges1) + 1, len(edges2) + 1
        adj1 = [[] for _ in range(n)]
        adj2 = [[] for _ in range(m)]
        for e in edges1:
            adj1[e[0]].append(e[1])
            adj1[e[1]].append(e[0])
        for e in edges2:
            adj2[e[0]].append(e[1])
            adj2[e[1]].append(e[0])

        depth1 = cal_depth(adj1, n)
        depth2 = cal_depth(adj2, m)
        ans = [0] * n
        for i in range(n):
            ans[i] = depth1[i][min(k, n - 1)]
            if k > 0:
                second_max = 0
                for j in range(m):
                    second_max = max(second_max, depth2[j][min(k - 1, m - 1)])
                ans[i] += second_max
        return ans


if __name__ == '__main__':

    Solution().maxTargetNodes([[5,2],[3,4],[7,3],[1,5],[0,1],[6,0],[6,7],[6,8]],[[5,0],[2,4],[3,2],[1,3],[1,5]],8)