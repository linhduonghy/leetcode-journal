from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [[] for _ in range(n)]
        connected = [[False] * n for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
            connected[edge[0]][edge[1]] = True
            connected[edge[1]][edge[0]] = True
        visited = [False] * n
        components = []
        def dfs(source: int, component_id: int):
            visited[source] = True
            components[component_id].append(source)
            for v in adj[source]:
                if not visited[v]:
                    dfs(v, component_id)
        
        component_id = 0
        for i in range(n):
            if not visited[i]:
                components.append([])
                dfs(i, component_id)
                component_id += 1

        def is_complete_component(component: List[int]):
            for u in range(len(component)):
                for v in range(u + 1, len(component)):
                    if not connected[component[u]][component[v]]:
                        return 0
            return 1
        
        count = 0
        for i in range(component_id):
            count += is_complete_component(components[i])
        
        return count