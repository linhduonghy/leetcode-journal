class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [None] * maxSize
        self.size = 0
        self.inc = [0] * maxSize

    def push(self, x: int) -> None:
        if not self.isFull():
            self.stack[self.size] = x
            self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        self.size -= 1
        if self.size > 0:
            self.inc[self.size - 1] += self.inc[self.size]
        x = self.stack[self.size] + self.inc[self.size] 
        self.inc[self.size] = 0
        return x

    def increment(self, k: int, val: int) -> None:
        k = min(self.size, k)
        
        self.inc[k - 1] += val
            
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.stack)
        

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)