from typing import List
from collections import deque

def get_component_cost(adj: List[tuple], source: int, visited: List[bool], connected_components: List[int], cnt: int):
    node_queue = deque()
    node_queue.append(source)
    cost = -1
    while node_queue:
        node = node_queue.popleft()
        connected_components[node] = cnt
        for neighbor, weight in adj[node]:
            cost &= weight
            if not visited[neighbor]:
                node_queue.append(neighbor)
                visited[neighbor] = True
    return cost      
    
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        
        adj = [[] for _ in range(n)]
        
        for edge in edges:
            adj[edge[0]].append((edge[1], edge[2]))
            adj[edge[1]].append((edge[0], edge[2]))
        
        visited = [False] * n
        
        connected_components = [-1] * n
        costs = []
        cnt = 0
        
        for i in range(n):
            if not visited[i]:
                costs.append(get_component_cost(adj, i, visited, connected_components, cnt))
                cnt += 1
        
        result = []
        for q in query:
            start, end = q[0], q[1]
            if connected_components[start] == connected_components[end]:
                result.append(costs[connected_components[start]])
            else:
                result.append(-1)
        
        return result
        