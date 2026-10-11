from typing import List
from collections import defaultdict
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        days_map = defaultdict(int)
        for meeting in meetings:
            days_map[meeting[0]] += 1
            days_map[meeting[1] + 1] -= 1
        
        days_list = sorted(days_map.keys())
        
        res = 0
        previous_day = 0
        prefix_sum = 0
        for i in range(0, len(days_list)):
            current_day = days_list[i]
            if prefix_sum == 0:
                res += current_day - previous_day
            prefix_sum += days_map[current_day]
            previous_day = current_day
        
        return res + days_list[0] - 1 + days - previous_day + 1
        