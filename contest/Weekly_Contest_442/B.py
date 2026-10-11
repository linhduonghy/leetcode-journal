from typing import List

def check_intersect(a: List[int], b: List[int], k: int) -> bool:
    cnt = 0
    aa = set(a)
    bb = set(b)
    for x in aa:
        for y in bb:
            if x == y:
                cnt += 1
    return cnt >= k

class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:

        n = len(properties)
        adj_list = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if check_intersect(properties[i], properties[j], k):
                    adj_list[i].append(j)
                    adj_list[j].append(i)

        visited = [False] * n
        def dfs(u: int):
            visited[u] = True
            for v in adj_list[u]:
                if not visited[v]:
                    dfs(v)

        res = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                res += 1

        return res


