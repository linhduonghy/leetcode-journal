from typing import List

def isCyclic(u: int, visit: List[bool], pathVisit: List[bool], adj: List[List[int]], topoOrdeR: List[int]) -> bool:

    visit[u] = True
    pathVisit[u] = True
        
    for v in adj[u]:
        if not visit[v]:
            if isCyclic(v, visit, pathVisit, adj, topoOrdeR):
                return True
        elif pathVisit[v]:
                return True

    pathVisit[u] = False
    topoOrdeR.append(u)
    
    return False

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
            
        adj = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
        
        visit = [False for _ in range(numCourses)]
        pathVisit = [False for _ in range(numCourses)]
        
        res = []
        for i in range(numCourses):
            if not visit[i]:
                if isCyclic(i, visit, pathVisit, adj, res):
                    return []
        print(res[::-1])
        return res[::-1]
        
        
if __name__ == "__main__":
    Solution().findOrder(4, [[0, 1], [0, 2], [3, 0]])
        