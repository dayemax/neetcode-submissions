class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)
        print(self.stack[-1])

    def pop(self) -> None:
        print(self.stack[-1])
        if not self.stack:
            return None
        self.min_stack.pop()
        print(self.stack[-1])
        return self.stack.pop()
        

    def top(self) -> int:
        print(self.stack[-1])
        return self.stack[-1]

    def getMin(self) -> int:
        print(self.min_stack[-1])
        return self.min_stack[-1]


