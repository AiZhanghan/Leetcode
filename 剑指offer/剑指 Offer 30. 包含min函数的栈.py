class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []

    def push(self, x):
        """
        Args:
            x: int
        """
        self.stack.append(x)
        if not self.helper or self.helper[-1] >= x:
            self.helper.append(x)

    def pop(self):
        if self.helper[-1] == self.stack.pop():
            self.helper.pop()

    def top(self):
        """
        Return:
            int
        """
        return self.stack[-1]

    def min(self):
        """
        Return:
            int
        """
        return self.helper[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()