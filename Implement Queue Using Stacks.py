class MyQueue:

    def __init__(self):
        self.queue=[]
        self.first = []
        self.last = 0

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.empty():
            return 0
        else:
            self.first = self.queue[::-1]
            self.temp = self.first.pop()
            self.queue = self.first[::-1]
            return self.temp
            
    def peek(self) -> int:
        if self.empty():
            return None
        else:
            self.last = self.queue[0]
            return self.last

    def empty(self) -> bool:
        if self.queue:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
