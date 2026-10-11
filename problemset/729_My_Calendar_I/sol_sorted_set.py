from sortedcontainers import SortedList


class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        end -= 1

        idx = self.calendar.bisect_right((start, end))
        if ((idx > 0 and start <= self.calendar[idx - 1][1]) or
                (idx < len(self.calendar) and end >= self.calendar[idx][0])):
            return False
        self.calendar.add((start, end))
        return True
