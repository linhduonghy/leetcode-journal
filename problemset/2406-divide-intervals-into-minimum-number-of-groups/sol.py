from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        events = []

        for interval in intervals:
            events.append((interval[0], 1))
            events.append((interval[1], -1))

        events.sort(key=lambda x: (x[0], x[1]))

        max_open = 0
        open_interval = 0
        for events in events:
            open_interval += events[1]
            max_open = max(max_open, open_interval)

        return max_open