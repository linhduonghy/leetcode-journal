from typing import List
from collections import deque, defaultdict


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


def bfs_distance(adj, start, target):
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        u, d = queue.popleft()
        if u == target:
            return d
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                queue.append((v, d + 1))


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        dsu = DSU(n)
        nums = [(num, index) for index, num in enumerate(nums)]
        nums.sort()
        adj = [[] for _ in range(n)]
        m = len(nums)
        i, j = 0, 1
        while i < m:
            while j < m and nums[j][0] - nums[i][0] <= maxDiff:
                j += 1
            for x in range(i, j):
                for y in range(i + 1, j):
                    adj[nums[x][1]].append(nums[y][1])
                    adj[nums[y][1]].append(nums[x][1])
                    dsu.union(nums[x][1], nums[y][1])
            i += 1

        components = defaultdict(list)
        for node in range(n):
            root = dsu.find(node)
            components[root].append(node)
        small_component_distances = {}
        SMALL_COMPONENT_THRESHOLD = 500
        for comp_id, nodes in components.items():
            if len(nodes) <= SMALL_COMPONENT_THRESHOLD:
                dist = {}
                for u in nodes:
                    queue = deque([(u, 0)])
                    visited = {u}
                    while queue:
                        node, d = queue.popleft()
                        dist[(u, node)] = d
                        for neighbor in adj[node]:
                            if neighbor not in visited:
                                visited.add(neighbor)
                                queue.append((neighbor, d + 1))
                small_component_distances[comp_id] = dist
        # Process queries
        result = []
        for u, v in queries:
            if dsu.find(u) != dsu.find(v):
                result.append(-1)
                continue

            comp_id = dsu.find(u)
            if comp_id in small_component_distances:
                result.append(small_component_distances[comp_id].get((u, v), -1))
            else:
                # Big component -> run BFS from u to find v
                result.append(bfs_distance(adj, u, v))

        return result
