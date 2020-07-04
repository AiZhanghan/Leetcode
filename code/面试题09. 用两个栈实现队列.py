class CQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def appendTail(self, value):
        """
        time: O(1)
        
        Args:
            value: int
        """
        self.in_stack.append(value)

    def deleteHead(self):
        """
        Return: int
        """
        if not self.in_stack and not self.out_stack:
            return -1
        
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        return self.out_stack.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()