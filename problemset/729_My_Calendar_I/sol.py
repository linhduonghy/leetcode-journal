class MyCalendar:

    def __init__(self):
        self.calender = []

    def book(self, start: int, end: int) -> bool:
        print(start, end)
        for x, y in self.calender:
            if not (end < x and start >= y):
                print(x, y)
                return False
        
        self.calender.append((start, end))
        
        return True