class MinStack:
    def __init__(self):
        self._stack=[]
        self._minVal=0
    
    def push(self, val: int) -> None:
        if self._stack == []:
            self._stack.append( val )
            self._minVal = val            
        elif val < self._minVal:
            self._stack.append( 2 * val - self._minVal)
            self._minVal = val
        else:
            self._stack.append(val)

    def pop(self) -> None:
        if self._stack == []:
            return
        elif self._stack[-1] < self._minVal:
            self._minVal = 2 * self._minVal - self._stack[-1]
        self._stack.pop()

    def top(self) -> int:
        if self._stack == []:
            return
        if self._stack[-1] < self._minVal:
            return self._minVal
        return self._stack[-1]

    def getMin(self) -> int:
        if self._stack == []:
            return
        return self._minVal
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
