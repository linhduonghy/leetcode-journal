from typing import List

def buildAdj(n: int, nums: List[int], maxDiff: int) -> List[List[int]]:
    adj = [[] for _ in range(n)]
    m = len(nums)
    i, j = 0, 1
    while i < m:
        while j < m and nums[j] - nums[i] <= maxDiff:
            adj[i].append(j)
            adj[j].append(i)
            j += 1
        i += 1
        if j <= i:
            j = i + 1
    return adj
def dfs(u: int, adj: List[List[int]], component: List[int], count: int, visited: List[bool]):
    component[u] = count
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs(v, adj, component, count, visited)
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        adj = buildAdj(n, nums, maxDiff)
        component = [-1 for _ in range(n)]
        count = 0
        visited = [False for _ in range(n)]
        for i in range(n):
            if not visited[i]:
                dfs(i, adj, component, count, visited)
                count += 1
        return [True if component[query[0]] == component[query[1]] else False for query in queries]