class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlap = []

    def book(self, start: int, end: int) -> bool:
        end -= 1
        for o in self.overlap:
            if self.is_overlap(start, end, o[0], o[1]):
                return False

        # add overlap booking
        for o in self.calendar:
            if self.is_overlap(start, end, o[0], o[1]):
                self.overlap.append(self.get_overlap(start, end, o[0], o[1]))

        # add to calendar
        self.calendar.append((start, end))

        return True

    def is_overlap(self, start1: int, end1: int, start2: int, end2: int) -> bool:
        return max(start1, start2) <= min(end1, end2)

    def get_overlap(self, start1: int, end1: int, start2: int, end2: int) -> tuple[int, int]:
        return max(start1, start2), min(end1, end2)

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)