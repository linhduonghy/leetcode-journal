from typing import List


def isCyclic(u: int, visit: List[bool], pathVisit: List[bool], adj: List[List[int]]):

    visit[u] = True
    pathVisit[u] = True
    for v in adj[u]:
        if not visit[v]:
            if isCyclic(v, visit, pathVisit, adj):
                return True
        elif pathVisit[v]:
            return True
    
    pathVisit[u] = False
    
    return False
        
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
        
        visit = [False for _ in range(numCourses)]
        pathVisit = [False for _ in range(numCourses)]
        
        for i in range(numCourses):
            if not visit[i]:
                if isCyclic(i, visit, pathVisit, adj):
                    return False
        
        return True