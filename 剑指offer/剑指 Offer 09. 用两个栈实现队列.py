class CQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def appendTail(self, value):
        """
        Args:
            value: int
        """
        self.in_stack.append(value)

    def deleteHead(self):
        """
        Return:
            int
        """
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop() if self.out_stack else -1
        

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()