from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.calender = SortedList()

    def book(self, start: int, end: int) -> bool:
        end -= 1
        
        
        
        self.calender.append((start, end))
        
        return True