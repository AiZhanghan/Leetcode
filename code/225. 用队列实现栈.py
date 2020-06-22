from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x):
        """
        Push element x onto stack.
        
        Args:
            x: int
        """
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        
        Return:
            int
        """
        return self.queue.popleft()

    def top(self):
        """
        Get the top element.
        
        Return:
            int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        
        Return:
            bool
        """
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()