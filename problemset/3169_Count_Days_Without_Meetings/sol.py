from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        meetings.sort(key = lambda e: (e[1], e[2]))
        
        ans = meetings[0][0] - 1
        
        i = 0
        ma = meetings[0][1]
        n = len(meetings)
        while i < n:
            j = i + 1
            while j < n and meetings[j][0] <= ma:
                ma = max(ma, meetings[j][1])
                j += 1
            if j < n:
                ans += meetings[j][0] - ma
            i = j
        
        return ans