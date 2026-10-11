from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        N = len(edges)
        adj = [[] for _ in range(N)]
        def is_connected(src: int, target: int, visited: List[bool], adj: List[List[int]]) -> bool:
            if src == target:
                return True
            visited[src] = True
            for u in adj[src]:
                if not visited[u]:
                    if is_connected(u, target, visited, adj):
                        return True
            return False

        for edge in edges:
            visited = [False] * N
            if is_connected(edge[0] - 1, edge[1] - 1, visited, adj):
                return edge
            adj[edge[0] - 1].append(edge[1] - 1)
            adj[edge[1] - 1].append(edge[0] - 1)