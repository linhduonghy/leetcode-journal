class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [None] * maxSize
        self.size = 0

    def push(self, x: int) -> None:
        if not self.isFull():
            self.stack[self.size] = x
            self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        self.size -= 1
        return self.stack[self.size]

    def increment(self, k: int, val: int) -> None:
        for i in range(0, min(k, self.size)):
            self.stack[i] += val
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.stack)
        

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)