class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack =[]
        self.out_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        
        Args:
            x: int
        """
        self.in_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        
        Return:
            int
        """
        if not self.out_stack:
            self.reload()
        return self.out_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        
        Return:
            int
        """
        if not self.out_stack:
            self.reload()
        return self.out_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not (self.in_stack or self.out_stack)

    def reload(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()