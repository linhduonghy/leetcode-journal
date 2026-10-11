from collections import deque

class MyCircularDeque:

    def __init__(self, k: int):
        self.dq = deque([], k)
        self.maxLen = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.dq.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.dq.append(value)
        return True
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.dq.popleft()
        return True
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.dq.pop()
        return True
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        x = self.dq.popleft()
        self.dq.appendleft(x)
        return x
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        x = self.dq.pop()
        self.dq.append(x)
        return x
    def isEmpty(self) -> bool:
        return len(self.dq) == 0
    def isFull(self) -> bool:
        return len(self.dq) == self.maxLen