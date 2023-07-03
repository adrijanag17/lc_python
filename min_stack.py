class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        curMin = self.getMin()
        if curMin == None or curMin < val:
            curMin = val
        # save the state - current minimum with each value
        self.stack.append((val, curMin))

    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1][0]


    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]
