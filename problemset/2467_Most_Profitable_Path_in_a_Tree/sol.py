from typing import List
from collections import deque

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
        n = len(amount)
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        bob_path = {}
        # dfs find the bob path
        def findBobPath(u: int, parent: int, step: int) -> bool:
            bob_path[u] = step
            if u == 0:
                return True
            for v in adj[u]:
                if v != parent:
                    if findBobPath(v, u, step + 1):
                        return True
            bob_path.pop(u, None)
            return False

        findBobPath(bob, -1, 0)
        # bfs find the alice path        
        q = deque([(0, -1, 0, 0)])
        max_income = float("-inf")
        
        while q:
            u, parent, step, income = q.popleft()
            
            if u not in bob_path or step < bob_path[u]:
                income += amount[u]
            elif step == bob_path[u]:
                income += amount[u] // 2
            
            if len(adj[u]) == 1 and u != 0:
                max_income = max(max_income, income)
            
            for v in adj[u]:
                if v != parent:
                    q.append((v, u, step + 1, income))
        
        return max_income
        
if __name__ == "__main__":
    Solution().mostProfitablePath([[0,1],[1,2],[1,3],[3,4]], 3, [-2,4,2,-4,6])
            

                