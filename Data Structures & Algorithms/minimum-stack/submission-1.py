class MinStack:

    def __init__(self):
        self.exStack = []
        self.dummy = []
        
    def push(self, val: int) -> None:

        self.exStack.append(val)

        if not self.dummy or val < self.dummy[-1]:
            self.dummy.append(val)
        else:
            self.dummy.append(self.dummy[-1])

    def pop(self) -> None:
        self.exStack.pop()
        self.dummy.pop()
        
    def top(self) -> int:
        return self.exStack[-1]

    def getMin(self) -> int:
        return self.dummy[-1]
        
